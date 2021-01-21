# -*- coding:utf-8 -*-
import os
import time
import re
from . import logger
from .client.qbittorrent import qBittorrent
from .client.transmission import Transmission
from .client.utorrent import uTorrent
from .client.deluge import Deluge
from .exception.nosuchclient import NoSuchClient
from .strategy import Strategy
from autoremovetorrents.torrent import Torrent

class Task(object):
    def __init__(self, name, conf, remove_torrents = True):
        # Logger
        self._logger = logger.Logger.register(__name__)

        # Save task name
        self._name = name

        # Replace environment variables first
        pattern = re.compile(r'\$\(([^\)]+)\)')
        replace_keys = ['host', 'username', 'password']
        for key in replace_keys:
            if key in conf:
                env = pattern.match(str(conf[key]))
                if env is not None and env.group(1) in os.environ:
                    conf[key] = os.environ[env.group(1)]

        # Read configurations
        self._client_name = conf['client']
        self._client = None
        self._host = conf['host'].rstrip('/')
        self._username = conf['username'] if 'username' in conf else ''
        self._password = conf['password'] if 'password' in conf else ''
        self._enabled_remove = remove_torrents
        self._delete_data = conf['delete_data'] if 'delete_data' in conf else False
        self._strategies = conf['strategies'] if 'strategies' in conf else []

        # Torrents
        self._torrents = set()
        self._remove = set()

        # Client status
        self._client_status = None

        # Allow removing specified torrents(for CI testing only)
        if 'force_delete' in conf:
            for hash_ in conf['force_delete']:
                torrent_obj = Torrent()
                torrent_obj.hash = hash_
                torrent_obj.name = hash_
                self._remove.add(torrent_obj)

        # Print debug logs
        self._logger.debug("Configuration of task '%s':" % self._name)
        self._logger.debug('Client: %s, Host: %s, Username: %s, Password: %s' % (
            self._client_name, self._host, self._username, self._password
        ))
        self._logger.debug('Remove Torrents: %s, Remove Torrents and Data: %s' % (
            self._enabled_remove, self._delete_data
        ))
        self._logger.debug('Strategies: %s' % ', '.join(self._strategies))

    # Login client
    def _login(self):
        # Find the type of client
        # Use unicode type for Python 2.7
        clients = {
            u'qbittorrent': qBittorrent,
            u'transmission': Transmission,
            u'μtorrent': uTorrent,
            u'utorrent': uTorrent, # Alias for μTorrent
            u'deluge': Deluge,
        }
        self._client_name = self._client_name.lower() # Set the client name to be case insensitive
        if self._client_name not in clients:
            raise NoSuchClient("The client `%s` doesn't exist." % self._client_name)

        # Initialize client object
        self._client = clients[self._client_name](self._host)

        # Login
        self._logger.info('Logging in...')
        self._client.login(self._username, self._password)
        self._logger.info('Login successfully. The client is %s.' % self._client.version())
        self._logger.info('WebUI API version: %s' % self._client.api_version())

        # Get client status
        self._client_status = self._client.client_status()
        self._logger.info(self._client_status)

    # Get all the torrents and properties
    def _get_torrents(self):
        self._logger.info('Getting all the torrents...')
        last_time = time.time()
        for hash_value in self._client.torrents_list():
            # Append new torrent
            self._torrents.add(self._client.torrent_properties(hash_value))
            # For a long waiting
            if time.time() - last_time > 1:
                self._logger.info('Please wait...We have found %d torrent(s).' %
                    len(self._torrents))
                last_time = time.time()
        self._logger.info('Found %d torrent(s) in the client.' % len(self._torrents))

    # Apply strategies
    def _apply_strategies(self):
        for strategy_name in self._strategies:
            strategy = Strategy(strategy_name, self._strategies[strategy_name])
            strategy.execute(self._client_status, self._torrents)
            self._remove.update(strategy.remove_list)

    # Remove torrents
    def _remove_torrents(self):
        # Bulid a dict to store torrent hashes and names which to be deleted
        delete_list = {}
        for torrent in self._remove:
            delete_list[torrent.hash] = torrent.name
        # Run deletion
        success, failed = self._client.remove_torrents([hash_ for hash_ in delete_list], self._delete_data)
        # Output logs
        for hash_ in success:
            self._logger.info(
                'The torrent %s and its data have been removed.' if self._delete_data \
                else 'The torrent %s has been removed.',
                delete_list[hash_]
            )
        for torrent in failed:
            self._logger.error('The torrent %s and its data cannot be removed. Reason: %s' if self._delete_data \
                else 'The torrent %s cannot be removed. Reason: %s',
                delete_list[torrent['hash']], torrent['reason']
            )

    # Execute
    def execute(self):
        self._logger.info("Running task '%s'..." % self._name)
        self._login()
        self._get_torrents()
        self._apply_strategies()
        if self._enabled_remove:
            self._remove_torrents()

    # Get remaining torrents (for tester)
    def get_remaining_torrents(self):
        return self._torrents

    # Get removed torrents (for tester)
    def get_removed_torrents(self):
        return self._remove