#-*- coding:utf-8 -*-
import requests
from ..torrent import Torrent
from ..clientstatus import ClientStatus
from ..torrentstatus import TorrentStatus
from ..portstatus import PortStatus
from ..exception.connectionfailure import ConnectionFailure
from ..exception.loginfailure import LoginFailure
from ..exception.nosuchclient import NoSuchClient
from ..exception.remotefailure import RemoteFailure

class Transmission(object):
    def __init__(self, host):
        # Host
        self._host = host
        # Request id
        self._request_id = 0
        # username & password
        self._username = None
        self._password = None
        # Requests Session
        self._session = requests.Session()

    # Login to Transmission
    def login(self, username, password):
        # Save authentication of session
        self._session.auth = (username, password)
    
    # Make Transmission Request
    def _make_transmission_request(self, method, arguments=None):
        retry = 3
        while retry > 0:
            retry -= 1
            # Make request
            try:
                request = self._session.post(self._host+'/transmission/rpc',
                    json={'method':method, 'arguments':arguments, 'tag':self._request_id})
                self._request_id += 1
            except Exception as exc:
                raise ConnectionFailure(str(exc))

            if request.status_code == 409: # Save Session ID and retry
                self._session.headers.update({
                    'X-Transmission-Session-Id': request.headers['X-Transmission-Session-Id']
                })
            elif request.status_code == 401: # Unauthorized user
                raise LoginFailure('Unauthorized user.')
            elif request.status_code == 200:
                result = request.json()
                if result['result'] == 'success': # Success
                    return result['arguments']
                else:
                    raise RemoteFailure(result['result'])
        raise RemoteFailure('The server responsed %d on method %s.' \
            % (request.status_code, method)
        )
    
    # Get client status
    def client_status(self):
        status = self._make_transmission_request('session-stats')

        cs = ClientStatus()
        # Remote free space checker
        cs.free_space = self.remote_free_space
        # Download speed and downloaded  size
        cs.download_speed = status['downloadSpeed']
        cs.total_downloaded = status['current-stats']['downloadedBytes']
        # Uploading speed and uploaded size
        cs.upload_speed = status['uploadSpeed']
        cs.total_uploaded = status['current-stats']['uploadedBytes']

        # Outgoing port status
        port_is_open = self._make_transmission_request('port-test')
        if port_is_open:
            cs.port_status = PortStatus.Open
        else:
            cs.port_status = PortStatus.Closed
        
        return cs
    
    # Get Transmission Version
    def version(self):
        ver = self._make_transmission_request('session-get')['version']
        return ('Transmission %s' % ver)
    
    # Get API Version
    def api_version(self):
        ver = self._make_transmission_request('session-get')['rpc-version']
        return str(ver)

    # Get Torrents List
    def torrents_list(self):
        torrents_hash = []
        for torrent in self._make_transmission_request('torrent-get', {'fields': ['hashString']})['torrents']:
            torrents_hash.append(torrent['hashString'])
        return torrents_hash

    # Get Torrent Properties
    def torrent_properties(self, torrent_hash):
        result = self._make_transmission_request('torrent-get',
            {
                'ids': [torrent_hash],
                'fields': [
                    'hashString',
                    'name',
                    'trackers',
                    'status',
                    'totalSize',
                    'uploadRatio',
                    'uploadedEver',
                    'addedDate',
                    'secondsSeeding',
                    'isStalled',
                    'error',
                    'labels',
                    'rateDownload',
                    'rateUpload',
                    'peersGettingFromUs',
                    'peersSendingToUs',
                    'trackerStats',
                    'activityDate',
                    'uploadedEver',
                    'secondsSeeding',
                    'downloadedEver',
                    'secondsDownloading',
                    'percentDone',
                ]}
            )
        if len(result['torrents']) == 0: # No such torrent
            raise NoSuchClient("No such torrent of hash '%s'." % torrent_hash)
        torrent = result['torrents'][0]
        # Create torrent object
        torrent_obj = Torrent()
        torrent_obj.hash = torrent['hashString']
        torrent_obj.name = torrent['name']
        if 'labels' in torrent:
            torrent_obj.category = torrent['labels']
        torrent_obj.tracker = [tracker['announce'] for tracker in torrent['trackers']]
        torrent_obj.status = Transmission._judge_status(torrent['status'], torrent['error'])
        torrent_obj.stalled = torrent['isStalled']
        torrent_obj.size = torrent['totalSize']
        torrent_obj.ratio = torrent['uploadRatio']
        torrent_obj.uploaded = torrent['uploadedEver']
        torrent_obj.downloaded = torrent['downloadedEver']
        torrent_obj.create_time = torrent['addedDate']
        torrent_obj.seeding_time = torrent['secondsSeeding']
        torrent_obj.upload_speed = torrent['rateUpload']
        torrent_obj.download_speed = torrent['rateDownload']
        torrent_obj.seeder = sum([tracker['seederCount'] for tracker in torrent['trackerStats']])
        torrent_obj.connected_seeder = torrent['peersSendingToUs']
        torrent_obj.leecher = sum([tracker['leecherCount'] for tracker in torrent['trackerStats']])
        torrent_obj.connected_leecher = torrent['peersGettingFromUs']
        torrent_obj.last_activity = torrent['activityDate']
        torrent_obj.average_upload_speed = torrent['uploadedEver'] / torrent['secondsSeeding'] if torrent['secondsSeeding'] != 0 else 0
        torrent_obj.average_download_speed = torrent['downloadedEver'] / torrent['secondsDownloading'] if torrent['secondsDownloading'] != 0 else 0
        torrent_obj.progress = torrent['percentDone']

        return torrent_obj
    
    # Get free space
    def remote_free_space(self, path):
        return self._make_transmission_request('free-space', {
            'path': path,
        })['size-bytes']

    # Judge Torrent Status
    @staticmethod
    def _judge_status(state, errno):
        if errno != 0:
            return TorrentStatus.Error
        else:
            return [
                TorrentStatus.Stopped,  # 0:STOPPED
                TorrentStatus.Queued,   # 1:CHECK_WAIT
                TorrentStatus.Checking, # 2:CHECK
                TorrentStatus.Queued,   # 3: DOWNLOAD_WAIT
                TorrentStatus.Downloading, # 4:DOWNLOAD
                TorrentStatus.Queued, # 5:SEED_WAIT
                TorrentStatus.Uploading, # 6:SEED
                TorrentStatus.Unknown # 7:ISOLATED(Torrent can't find peers)
            ][state]

    # Batch Remove Torrents
    # Return values: (success_hash_list, failed_hash_list : {hash: reason, ...})
    def remove_torrents(self, torrent_hash_list, remove_data):
        try:
            self._make_transmission_request('torrent-remove',
                {'ids': torrent_hash_list, 'delete-local-data': remove_data})
        except Exception as e:
            # We couldn't judge which torrents are removed and which aren't when an exception was raised
            # Therefore we think all the deletion have been failed
            return ([], [{
                'hash': torrent,
                'reason': str(e),
            } for torrent in torrent_hash_list])
        return (torrent_hash_list, [])
