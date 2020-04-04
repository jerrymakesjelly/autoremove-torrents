# -*- coding:utf-8 -*-

from .sortbase import ConditionWithSort
from autoremovetorrents.compatibility.disk_usage_ import disk_usage_

class FreeSpaceCondition(ConditionWithSort):
    def __init__(self, settings):
        ConditionWithSort.__init__(self, settings['action'])
        self._min = settings['min'] * 1073741824  # limit = limit * 1GiB
        self._path = settings['path']

    def apply(self, torrents):
        torrents = list(torrents)
        ConditionWithSort.sort_torrents(self, torrents)
        free_space = disk_usage_(self._path)['free']
        for torrent in torrents:
            if free_space < self._min:
                free_space += torrent.size
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)
