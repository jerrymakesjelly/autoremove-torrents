#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logger
import yaml
import time
import sys
import urllib.parse
from client.qbittorrent import qBittorrent
from client.transmission import Transmission
from client.utorrent import uTorrent
from client.base.torrentstatus import TorrentStatus

class AutoRemover(object):
    def __init__(self, conf_path):
        # Logger
        self._logger = logger.register(__name__)
        # Configurations
        self._config = self._load_configurations(conf_path)
    
    # Load Configurations
    def _load_configurations(self, conf_path):
        self._logger.info('Loading configurations...')
        with open(conf_path, 'r') as stream:
            result = yaml.safe_load(stream)
        self._logger.info('Found %d task(s) in the file.' % len(result))
        return result

    # Get the client handle
    def _client_handle(self, client_name, host):
        if client_name.lower() == 'qbittorrent':
            return qBittorrent(host)
        elif client_name.lower() == 'transmission':
            return Transmission(host)
        elif client_name.lower() == 'utorrent':
            return uTorrent(host)
        else:
            raise RuntimeError('Unknown Client.')

    # Execute
    def execute(self, task_name=None):
        result = []
        if task_name == None:
            for task in self._config:
                result.append(self._execute_task(task))
        else:
            result.append(self._execute_task(task_name))
        return result
    
    # Execute a task
    def _execute_task(self, task_name):
        # Get the task
        self._logger.info('%s is running.' % task_name)
        task = self._config[task_name]
        # Login the client
        self._logger.info('Logging in...')
        client = self._client_handle(task['client'], task['host'])
        client.login(task['username'], task['password'])
        # Show the version
        self._logger.info('Login successfully. The client is %s.' % client.version())
        
        # Get all the torrents and properties
        self._logger.info('Getting all the torrents...')
        all_torrents = dict()
        last_time = time.time() # For a long time to wait
        for hash in client.torrents_list():
            torrent = client.torrent_properties(hash)
            all_torrents[hash] = torrent
            if time.time() - last_time > 10:
                self._logger.info('Please wait...We have found %d seed(s)...' % len(all_torrents))
                last_time = time.time()
        self._logger.info('Found %d seed(s) in the client.' % len(all_torrents))
        torrents = [all_torrents[hash] for hash in all_torrents]

        # Apply the filters to each strategy
        final_tbd = [] # To be deleted
        for strategy_name in task['strategies']:
            tbd = self._execute_strategy(task_name, strategy_name, torrents)
            # Add to final list
            final_tbd.extend(tbd)
            # Remove them from the torrent list
            for seed in tbd:
                torrents.remove(seed)
        # Print the remaining seeds
        #self._logger.info("%d seed(s) left." % len(torrents))
        #for seed in torrents:
        #    self._logger.info(self._format_torrent_info(seed))
        # Generate a list
        return {
            'task':task_name, 
            'hash':[seed['hash'] for seed in final_tbd],
            'name':[seed['name'] for seed in final_tbd]
        }
    
    # Execute a strategy
    def _execute_strategy(self, task_name, strategy_name, torrents):
        self._logger.info('Processing strategy %s...' % strategy_name)
        strategy = self._config[task_name]['strategies'][strategy_name]
        reject = None
        tbd = []
        # Apply category filter
        if 'all_categories' in strategy or 'categories' in strategy:
            torrents = self._category_filter(torrents, 
                strategy['categories'] if 'categories' in strategy else [],
                strategy['excluded_categories'] if 'excluded_categories' in strategy else [],
                strategy['all_categories'] if 'all_categories' in strategy else not 'categories' in strategy)
        # Apply tracker filter
        if 'all_trackers' in strategy or 'trackers' in strategy:
            torrents = self._tracker_filter(torrents,
                strategy['trackers'] if 'trackers' in strategy else [],
                strategy['excluded_trackers'] if 'excluded_trackers' in strategy else[],
                strategy['all_trackers'] if 'all_trackers' in strategy else not 'trackers' in strategy)
        total = len(torrents)
        # Apply seeding time filter
        if 'seeding_time' in strategy:
            torrents, reject = self._seeding_time_filter(torrents, strategy['seeding_time'])
            tbd.extend(reject)
        # Apply creation time filter
        if 'create_time' in strategy:
            torrents, reject = self._creation_time_filter(torrents, strategy['create_time'])
            tbd.extend(reject)
        # Apply ratio filter
        if 'ratio' in strategy:
            torrents, reject = self._ratio_filter(torrents, strategy['ratio'])
            tbd.extend(reject)
        # Apply seed size filter
        if 'seed_size' in strategy:
            torrents, reject = self._seed_size_filter(torrents, 
                strategy['seed_size']['limit'], strategy['seed_size']['action'])
            tbd.extend(reject)
        # Print the result
        self._logger.info("Total: %d seed(s). %d seed(s) can be removed." % (total, len(tbd)))
        for seed in tbd:
            self._logger.info(self._format_torrent_info(seed))
        return tbd
            
    # Convert Seconds
    def _convert_seconds(self, sec):
        if sec == -1:
            return '(Not Provided)'
        else:
            m, s = divmod(sec, 60)
            h, m = divmod(m, 60)
            d, h = divmod(h, 24)
            return ('%dd %02d:%02d:%02d' % (d, h, m, s))

    # Convert Bytes
    def _convert_bytes(self, byte):
        units = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB'
            'YiB', 'BiB', 'NiB', 'DiB', 'CiB']
        for x in units:
            if divmod(byte, 1024)[0] == 0:
                break
            else:
                byte /= 1024
        return ('%.2lf%s' % (byte, x))
    
    # Convert Timestamp
    def _convert_timestamp(self, timestamp):
        return '(Not Provided)' if timestamp == sys.maxsize \
            else time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    
    # Print torrent's information
    def _format_torrent_info(self, seed):
        return "%s\nSize:%s\tRatio:%.3f\tTotal Uploaded:%s\tSeeding Time:%s\tCategory:%s\nCreate Time:%s" % \
            (seed['name'], self._convert_bytes(seed['size']), seed['ratio'],
            self._convert_bytes(seed['uploaded']),
            self._convert_seconds(seed['seeding_time']), 
            seed['category'], self._convert_timestamp(seed['create_time']))
    
    # Category Filter
    def _category_filter(self, seeds, categories, excepts, all_categories=False):
        return [seed for seed in seeds if (all_categories or seed['category'] in categories) and not (seed['category'] in excepts)]
    
    # Tracker Filter
    def _tracker_filter(self, seeds, trackers, excepts, all_trackers=False):
        result = []
        # Filter eligible trackers
        for seed in seeds:
            for tracker in seed['tracker']: # For each tracker
                tracker = urllib.parse.urlparse(tracker).netloc
                if all_trackers or tracker in trackers:
                    result.append(seed)
                if tracker in excepts:
                    result.remove(seed)
                    break # Reject this seed
        return result
    
    # Seeding Time Filter
    def _seeding_time_filter(self, seeds, seeding_time):
        accept = []
        reject = []
        for seed in seeds:
            if seed['status'] != TorrentStatus.Uploading or seed['seeding_time'] <= seeding_time:
                accept.append(seed)
            else:
                reject.append(seed)
        return (accept, reject)

    # Creation Time Filter
    def _creation_time_filter(self, seeds, creation_time):
        accept = []
        reject = []
        for seed in seeds:
            if time.time() - seed['create_time'] <= creation_time:
                accept.append(seed)
            else:
                reject.append(seed)
        return (accept, reject)
    
    # Ratio Filter
    def _ratio_filter(self, seeds, ratio):
        accept = []
        reject = []
        for seed in seeds:
            if seed['status'] != TorrentStatus.Uploading or seed['ratio'] <= ratio:
                accept.append(seed)
            else:
                reject.append(seed)
        return (accept, reject)
    
    # Seed Size Filter
    def _seed_size_filter(self, seeds, limit, action):
        # Sort the seeds to calculate their size
        if action == 'remove-old-seeds':
            seeds.sort(key=lambda seed: seed['create_time'], reverse=True)
        elif action == 'remove-new-seeds':
            seeds.sort(key=lambda seed: seed['create_time'], reverse=False)
        elif action == 'remove-big-seeds':
            seeds.sort(key=lambda seed: seed['size'], reverse=False)
        elif action == 'remove-small-seeds':
            seeds.sort(key=lambda seed: seed['size'], reverse=True)

        # Calculate the size of the seeds
        sum = 0
        limit *= 1073741824 # 1GB = 2^30B
        accept = []
        reject = []
        for seed in seeds:
            if sum+seed['size'] < limit:
                sum += seed['size']
                accept.append(seed)
            else:
                reject.append(seed)
        return (accept, reject)
    
    # Remove Torrents
    def remove(self, remove_list):
        for item in remove_list:
            task = self._config[item['task']]
            # Get the client and log in
            client = self._client_handle(task['client'], task['host'])
            client.login(task['username'], task['password'])
            # Remove seeds
            if 'delete_data' in task and task['delete_data']:
                for i in range(len(item['hash'])):
                    client.remove_data(item['hash'][i])
                    self._logger.info('The torrent %s and its data have been removed.',
                        item['name'][i])
            else:
                for i in range(len(item['hash'])):
                    client.remove_torrent(item['hash'][i])
                    self._logger.info('The torrent %s has been removed.', item['name'][i])