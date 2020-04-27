#-*- coding:utf-8 -*-

from .base import Comparer
from .base import Condition
from ..torrentstatus import TorrentStatus

class RatioCondition(Condition):
    def __init__(self, r, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._ratio = r
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.ratio, self._ratio, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)