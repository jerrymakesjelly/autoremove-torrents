#-*- coding:utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
from ..torrent import Torrent
from ..torrentstatus import TorrentStatus
from ..exception.connectionfailure import ConnectionFailure
from ..exception.deletionfailure import DeletionFailure
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
        torrent_obj.size = torrent['totalSize']
        torrent_obj.ratio = torrent['uploadRatio']
        torrent_obj.uploaded = torrent['uploadedEver']
        torrent_obj.create_time = torrent['addedDate']
        torrent_obj.seeding_time = torrent['secondsSeeding']
        torrent_obj.upload_speed = torrent['rateUpload']
        torrent_obj.download_speed = torrent['rateDownload']
        torrent_obj.seeder = sum([tracker['seederCount'] for tracker in torrent['trackerStats']])
        torrent_obj.connected_seeder = torrent['peersSendingToUs']
        torrent_obj.leecher = sum([tracker['leecherCount'] for tracker in torrent['trackerStats']])
        torrent_obj.connected_leecher = torrent['peersGettingFromUs']
        torrent_obj.last_activity = torrent['activityDate']
        torrent_obj.average_upload_speed = torrent['uploadedEver'] / torrent['secondsSeeding']
        torrent_obj.average_download_speed = torrent['downloadedEver'] / torrent['secondsDownloading']
        torrent_obj.progress = torrent['percentDone']

        return torrent_obj

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

    # Remove Torrent
    def remove_torrent(self, torrent_hash):
        try:
            self._make_transmission_request('torrent-remove',
                    {'ids':[torrent_hash], 'delete-local-data':False})
        except Exception as e:
            raise DeletionFailure('Cannot delete torrent %s. %s' % (torrent_hash, str(e)))
    
    # Remove Data
    def remove_data(self, torrent_hash):
        try:
            self._make_transmission_request('torrent-remove',
                    {'ids':[torrent_hash], 'delete-local-data':True})
        except Exception as e:
            raise DeletionFailure('Cannot delete torrent %s and its data. %s' % (torrent_hash, str(e)))