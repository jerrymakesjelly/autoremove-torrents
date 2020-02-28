#-*- coding:utf-8 -*-
import re
import time
from requests.auth import HTTPBasicAuth
import requests
from ..torrent import Torrent
from autoremovetorrents.exception.connectionfailure import ConnectionFailure
from autoremovetorrents.exception.deletionfailure import DeletionFailure
from autoremovetorrents.exception.loginfailure import LoginFailure
from autoremovetorrents.exception.nosuchtorrent import NoSuchTorrent
from autoremovetorrents.exception.remotefailure import RemoteFailure
from ..torrentstatus import TorrentStatus

class uTorrent(object):
    def __init__(self, host):
        # Token
        self._token = ''
        # uTorrent version
        self._version = ''
        # Request Session
        self._session = requests.Session()
        # Server information
        self._host = host
        # Torrents list cache
        self._torrents_list_cache = []
        self._refresh_cycle = 30
        self._refresh_time = 0

    # Login to uTorrent
    def login(self, username, password):
        # HTTP Authorization
        self._session.auth = (username, password)
        # Requests Token
        try:
            request = self._session.get(self._host+'/gui/token.html')
        except Exception as exc:
            raise ConnectionFailure(str(exc))
        
        pattern = re.compile('<[^>]+>')
        text = request.text
        if request.status_code == 200:     
            self._token = pattern.sub('', text)
        elif request.status_code == 401: # Error
            raise LoginFailure('401 Unauthorized.')
        else:
            raise RemoteFailure('The server responsed %d.' \
                % request.status_code)
    
    # Get uTorrent Version
    def version(self):
        if self._version == '': # Call torrents_list() to get the version
            self.torrents_list()
        return ('uTorrent (bulid %s)' % str(self._version))
    
    # Get API Version
    def api_version(self):
        return 'Unknown' # There is no interfaces to check the API version
    
    # Get Torrents List
    def torrents_list(self):
        # Request torrents list
        torrents_hash = []
        request = self._session.get(self._host+'/gui/', params={'list':1, 'token':self._token})
        request.encoding = 'utf-8'
        if request.status_code != 200: # Error
            raise RemoteFailure('The server reponsed %s.' % request.text)
        result = request.json()
        self._torrents_list_cache = result
        self._refresh_time = time.time()
        # Get version
        self._version = result['build']
        # Get hash for each torrent
        for torrent in result['torrents']:
            torrents_hash.append(torrent[0])
        return torrents_hash
    
    # Get Torrent Job Properties
    def _torrent_job_properties(self, torrent_hash):
        request = self._session.get(self._host+'/gui/',
            params={'action':'getprops', 'token':self._token, 'hash':torrent_hash})
        request.encoding = 'utf-8'
        return request.json()['props'][0]
    
    # Get Torrent Properties
    def torrent_properties(self, torrent_hash):
        if time.time() - self._refresh_time > self._refresh_cycle: # Refresh
            self.torrents_list()
        for torrent in self._torrents_list_cache['torrents']:
            if torrent[0] == torrent_hash:
                # Properties
                properties = self._torrent_job_properties(torrent_hash)
                # Create torrent object
                torrent_obj = Torrent()
                torrent_obj.hash = torrent[0]
                torrent_obj.name = torrent[2]
                # The category list will be empty if a torrent was not specified categories
                torrent_obj.category = [torrent[11]] if len(torrent[11]) > 0 else []
                torrent_obj.tracker = properties['trackers'].split()
                torrent_obj.status = uTorrent._judge_status(torrent[1], torrent[4])
                torrent_obj.size = torrent[3]
                torrent_obj.ratio = torrent[7]/1000
                torrent_obj.uploaded = torrent[6]
                torrent_obj.seeding_time = torrent[6]
                torrent_obj.upload_speed = properties['ulrate']
                torrent_obj.download_speed = properties['dlrate']
                torrent_obj.seeder = torrent[15]
                torrent_obj.connected_seeder = torrent[14]
                torrent_obj.leecher = torrent[13]
                torrent_obj.connected_leecher = torrent[12]
                torrent_obj.progress = torrent[4]
                
                return torrent_obj
        # Not Found
        raise NoSuchTorrent('No such torrent.')

    # Judge Torrent Status
    @staticmethod
    def _judge_status(state, progress):
        if state & 32: # Paused
            status = TorrentStatus.Paused
        elif state & 1: # Started
            if progress == 1000: # Progess: 100.0%
                status = TorrentStatus.Uploading
            else:
                status = TorrentStatus.Downloading
        elif state & 2: # Checking
            status = TorrentStatus.Checking
        elif state & 16: # Error
            status = TorrentStatus.Error
        elif state & 64: # Queued
            status = TorrentStatus.Queued
        elif state & 128: # Loaded
            status = TorrentStatus.Stopped
        else:
            status = TorrentStatus.Unknown
        return status
    
    # Remove Torrent
    def remove_torrent(self, torrent_hash):
        request = self._session.get(self._host+'/gui/',
            params={'action':'remove', 'token':self._token, 'hash':torrent_hash})
        if request.status_code != 200:
            raise DeletionFailure('Cannot delete torrent %s. The server responses HTTP %d.' % (torrent_hash, request.status_code))
    
    # Remove Torrent and Data
    def remove_data(self, torrent_hash):
        request = self._session.get(self._host+'/gui/',
            params={'action':'removedata', 'token':self._token, 'hash':torrent_hash})
        if request.status_code != 200:
            raise DeletionFailure('Cannot delete torrent %s and its data. The server responses HTTP %d.' % (torrent_hash, request.status_code))