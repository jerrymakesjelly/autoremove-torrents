#-*- coding:utf-8 -*-
import requests
import time
from ..torrent import Torrent
from ..torrentstatus import TorrentStatus
from ..exception.loginfailure import LoginFailure
from ..exception.deletionfailure import DeletionFailure
from ..exception.connectionfailure import ConnectionFailure

class qBittorrent(object):
    def __init__(self, host):
        # Host
        self._host = host
        # Requests Session
        self._session = requests.Session()
        # Host
        self._host = host
        # Torrents list cache
        self._torrents_list_cache = []
        self._refresh_cycle = 30
        self._refresh_time = 0

    # Login to qBittorrent
    def login(self, username, password):
        try:
            request = self._session.post(self._host+'/login', data={'username':username, 'password':password})
        except Exception as exc:
            raise ConnectionFailure(str(exc))
        
        if request.status_code == 200:
            if request.text == 'Fails.': # Fail
                raise LoginFailure(request.text)
        else:
            raise LoginFailure('The server returned HTTP %d.' % request.status_code)
    
    # Get qBittorrent Version
    def version(self):
        request = self._session.get(self._host+'/version/qbittorrent')
        return ('qBittorrent %s' % request.text)
    
    # Get Torrents List
    def torrents_list(self):
        # Request torrents list
        torrent_hash = []
        request = self._session.get(self._host+'/query/torrents')
        result = request.json()
        # Save to cache
        self._torrents_list_cache = result
        self._refresh_time = time.time()
        # Get hash for each torrent
        for torrent in result:
            torrent_hash.append(torrent['hash'])
        return torrent_hash

    # Get Torrent's Generic Properties
    def _torrent_generic_properties(self, torrent_hash):
        return self._session.get(self._host+'/query/propertiesGeneral/'+torrent_hash).json()
    
    # Get Torrent's Tracker
    def _torrent_trackers(self, torrent_hash):
        return self._session.get(self._host+'/query/propertiesTrackers/'+torrent_hash).json()
    
    # Get Torrent Properties
    def torrent_properties(self, torrent_hash):
        if time.time() - self._refresh_time > self._refresh_cycle: # Out of date
            self.torrents_list()
        for torrent in self._torrents_list_cache:
            if torrent['hash'] == torrent_hash:
                # Get other information
                properties = self._torrent_generic_properties(torrent_hash)
                trackers = self._torrent_trackers(torrent_hash)
                return Torrent(
                    torrent['hash'], torrent['name'],
                    torrent['category'] if 'category' in torrent else torrent['label'],
                    [tracker['url'] for tracker in trackers],
                    qBittorrent._judge_status(torrent['state']), 
                    torrent['state'] == 'stalledUP' or torrent['state'] == 'stalledDL',
                    torrent['size'], torrent['ratio'],
                    properties['total_uploaded'], properties['addition_date'],
                    properties['seeding_time'])

    # Judge Torrent Status (qBittorrent doesn't have stopped status)
    @staticmethod
    def _judge_status(state):
        if state == 'downloading' or state == 'stalledDL':
            status = TorrentStatus.Downloading
        elif state == 'queuedDL' or state == 'queuedUP':
            status = TorrentStatus.Queued
        elif state == 'uploading' or state == 'stalledUP':
            status = TorrentStatus.Uploading
        elif state == 'checkingUP' or state == 'checkingDL':
            status = TorrentStatus.Checking
        elif state == 'pausedUP' or state == 'pausedDL':
            status = TorrentStatus.Paused
        else:
            status = TorrentStatus.Unknown
        return status
    
    # Remove Torrent
    def remove_torrent(self, torrent_hash):
        self._session.post(self._host+'/command/delete', data={'hashes':torrent_hash})
    
    # Remove Torrent and Data
    def remove_data(self, torrent_hash):
        self._session.post(self._host+'/command/deletePerm', data={'hashes':torrent_hash})