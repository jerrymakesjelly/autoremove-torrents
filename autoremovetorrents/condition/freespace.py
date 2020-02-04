# -*- coding:utf-8 -*-

from .sortbase import ConditionWithSort
import psutil


class FreeSpaceCondition(ConditionWithSort):
    def __init__(self, settings):
        ConditionWithSort.__init__(self, settings['action'])
        self._min = settings['min'] * 1073741824  # limit = limit * 1GiB
        self._path = settings['path']

    def apply(self, torrents):
        torrents = list(torrents)
        ConditionWithSort.sort_torrents(self, torrents)
        _, _, free_space, _ = psutil.disk_usage(self._path)
        for torrent in torrents:
            if free_space < self._min:
                free_space += torrent.size
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)
