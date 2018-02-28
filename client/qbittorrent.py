#-*- coding:utf-8 -*-
import logging
import requests
import time
from .base.clientbase import ClientBase
from .base.torrentstatus import TorrentStatus

class qBittorrent(ClientBase):
    def __init__(self, host):
        # Logger
        self._logger = logging.getLogger(__name__)
        # Host
        self._host = host
        # Cookies
        self._cookies = None
        # Host
        self._host = host
        # Torrents list cache
        self._torrents_list_cache = []
        self._refresh_cycle = 30
        self._refresh_time = 0
    
    # Login to qBittorrent
    def login(self, username, password):
        request = requests.post(self._host+'/login', data={'username':username, 'password':password})
        self._logger.info(request.text)
        if request.status_code == 200:
            if request.text == 'Ok.': # Success
                self._cookies = request.cookies
            else:
                raise RuntimeError(request.text)
        else:
            raise RuntimeError('HTTP Error')
    
    # Get qBittorrent Version
    def version(self):
        request = requests.get(self._host+'/version/qbittorrent', cookies=self._cookies)
        return ('qBittorrent %s' % request.text)
    
    # Get Torrents List
    def torrents_list(self):
        # Request torrents list
        torrent_hash = []
        request = requests.get(self._host+'/query/torrents', cookies=self._cookies)
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
        return requests.get(self._host+'/query/propertiesGeneral/'+torrent_hash,
            cookies=self._cookies).json()
    
    # Get Torrent's Tracker
    def _torrent_trackers(self, torrent_hash):
        return requests.get(self._host+'/query/propertiesTrackers/'+torrent_hash,
            cookies=self._cookies).json()
    
    # Get Torrent Properties
    def torrent_properties(self, torrent_hash):
        if time.time() - self._refresh_time > self._refresh_cycle: # Out of date
            self.torrents_list()
        for torrent in self._torrents_list_cache:
            if torrent['hash'] == torrent_hash:
                # Judge Status(qBittorrent doesn't have stopped status)
                state = torrent['state']
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
                # Get other information
                properties = self._torrent_generic_properties(torrent_hash)
                trackers = self._torrent_trackers(torrent_hash)
                return ClientBase._torrent_properties(self,
                    torrent['hash'], torrent['name'], 
                    torrent['category'] if 'category' in torrent else torrent['label'],
                    [tracker['url'] for tracker in trackers],
                    status, torrent['size'], torrent['ratio'],
                    properties['total_uploaded'], properties['addition_date'],
                    properties['seeding_time'])
    
    # Remove Torrent
    def remove_torrent(self, torrent_hash):
        requests.post(self._host+'/command/delete', 
            data={'hashes':torrent_hash}, cookies=self._cookies)
    
    # Remove Torrent and Data
    def remove_data(self, torrent_hash):
        requests.post(self._host+'/command/deletePerm',
            data={'hashes':torrent_hash}, cookies=self._cookies)