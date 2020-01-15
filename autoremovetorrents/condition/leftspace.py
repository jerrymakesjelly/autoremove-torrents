# -*- coding:utf-8 -*-

from .base import Condition
from .sortbase import ConditionWithSort
import shutil


class LeftSpaceCondition(Condition):
    def __init__(self, settings):
        ConditionWithSort.__init__(self, settings['action'])
        self._limit = settings['limit'] * 1073741824  # limit = limit * 1GiB
        self._path = settings['path']

    def apply(self, torrents):
        torrents = list(torrents)
        ConditionWithSort.sort_torrents(self, torrents)
        torrents = reversed(torrents)
        _, _, left_space = shutil.disk_usage(self._path)
        for torrent in torrents:
            if left_space < self._limit:
                left_space += torrent.size
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)
