# -*- coding:utf-8 -*-
import sys
import os
import time
import re
import yaml
from . import logger
from .client.qbittorrent import qBittorrent
from .client.transmission import Transmission
from .client.utorrent import uTorrent
from .exception.nosuchclient import NoSuchClient
from .strategy import Strategy
from autoremovetorrents.torrent import Torrent
from autoremovetorrents.torrentstatus import TorrentStatus

class Task(object):
    # Logger
    _logger = logger.register(__name__)

    def __init__(self, name, conf, remove_torrents = True):

        # Save task name
        self._name = name

        # Replace environment variables first
        pattern = re.compile('\$\(([^\)]+)\)')
        replace_keys = ['host', 'username', 'password']
        for key in replace_keys:
            if key in conf:
                env = pattern.match(conf[key])
                if env is not None and env.group(1) in os.environ:
                    conf[key] = os.environ[env.group(1)]

        # Read configurations
        self._client_name = conf['client']
        self._client = None
        self._host = conf['host']
        self._username = conf['username'] if 'username' in conf else ''
        self._password = conf['password'] if 'password' in conf else ''
        self._enabled_remove = remove_torrents
        self._delete_data = conf['delete_data'] if 'delete_data' in conf else False
        self._strategies = conf['strategies'] if 'strategies' in conf else []

        # Torrents
        self._torrents = []
        self._remove = []

        # Allow removing specified torrents
        if 'force_delete' in conf:
            for hash in conf['force_delete']:
                self._remove.append(Torrent(
                    hash,
                    hash,
                    '(No Category)',
                    [],
                    TorrentStatus.Unknown,
                    0,
                    0,
                    0,
                    sys.maxsize, # No create time
                    -1 # No seeding time
                ))

    # Login client
    def _login(self):
        # Find the type of client
        clients = [qBittorrent, Transmission, uTorrent]
        client_names = ['qbittorrent', 'transmission', 'utorrent']
        for i in range(0, len(client_names)):
            if self._client_name == client_names[i]:
                self._client = clients[i](self._host)
                break

        # Login
        self._logger.info('Logging in...')
        if self._client != None:
            self._client.login(self._username, self._password)
        else:
            raise NoSuchClient("The client `%s` doesn't exist." % self._client_name)
        self._logger.info('Login successfully. The client is %s.' % self._client.version())

    # Get all the torrents and properties
    def _get_torrents(self):
        self._logger.info('Getting all the torrents...')
        last_time = time.time()
        for hash_value in self._client.torrents_list():
            # Append new torrent
            self._torrents.append(self._client.torrent_properties(hash_value))
            # For a long waiting
            if time.time() - last_time > 10:
                self._logger.info('Please wait...We have found %d seed(s).' %
                    len(self._torrents))
                last_time = time.time()
        self._logger.info('Found %d seed(s) in the client.' % len(self._torrents))

    # Apply strategies
    def _apply_strategies(self):
        for strategy_name in self._strategies:
            strategy = Strategy(strategy_name, self._strategies[strategy_name])
            strategy.execute(self._torrents)
            #self._torrents = strategy.remain_list
            self._remove.extend(strategy.remove_list)

    # Remove torrents
    def _remove_torrents(self):
        for torrent in self._remove:
            if self._delete_data:
                self._client.remove_data(torrent.hash)
                self._logger.info('The torrent %s and its data have been removed.', torrent.name)
            else:
                self._client.remove_torrent(torrent.hash)
                self._logger.info('The torrent %s has been removed.', torrent.name)

    # Execute
    def execute(self):
        self._logger.info("Running task '%s'..." % self._name)
        self._login()
        self._get_torrents()
        self._apply_strategies()
        if self._enabled_remove:
            self._remove_torrents()
