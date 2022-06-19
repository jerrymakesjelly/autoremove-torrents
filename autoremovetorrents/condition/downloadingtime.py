#-*- coding:utf-8 -*-

from .base import Comparer
from .base import Condition

class DownloadingTimeCondition(Condition):
    def __init__(self, dt, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._downloading_time = dt
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.downloading_time, self._downloading_time, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)