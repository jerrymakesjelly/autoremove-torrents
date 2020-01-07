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
            {'ids': [torrent_hash],
            'fields': ['hashString', 'name', 'trackers', 'status', 'totalSize', 'uploadRatio', 'uploadedEver', 'addedDate', 'secondsSeeding', 'isStalled']}
            )
        if len(result['torrents']) == 0: # No such torrent
            raise NoSuchClient("No such torrent of hash '%s'." % torrent_hash)
        torrent = result['torrents'][0]
        return Torrent(
            torrent['hashString'], torrent['name'], '',
            [tracker['announce'] for tracker in torrent['trackers']],
            Transmission._judge_status(torrent['status']), 
            torrent['isStalled'],
            torrent['totalSize'], torrent['uploadRatio'],
            torrent['uploadedEver'], torrent['addedDate'], torrent['secondsSeeding'])

    # Judge Torrent Status
    @staticmethod
    def _judge_status(state):
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