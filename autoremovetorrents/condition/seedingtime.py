#-*- coding:utf-8 -*-

from .base import Comparer
from .base import Condition
from ..torrentstatus import TorrentStatus

class SeedingTimeCondition(Condition):
    def __init__(self, st, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._seeding_time = st
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.seeding_time, self._seeding_time, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)