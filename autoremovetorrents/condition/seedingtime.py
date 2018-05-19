#-*- coding:utf-8 -*-

from .base import Condition
from ..torrentstatus import TorrentStatus

class SeedingTimeCondition(Condition):
    def __init__(self, st):
        Condition.__init__(self) # Initialize remain and remove list
        self._seeding_time = st
    
    def apply(self, torrents):
        for torrent in torrents:
            if torrent.status == TorrentStatus.Uploading and \
                torrent.seeding_time > self._seeding_time:
                self.remove.append(torrent)
            else:
                self.remain.append(torrent)