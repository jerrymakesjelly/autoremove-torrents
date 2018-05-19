#-*- coding:utf-8 -*-

from .base import Condition
from ..torrentstatus import TorrentStatus

class RatioCondition(Condition):
    def __init__(self, r):
        Condition.__init__(self) # Initialize remain and remove list
        self._ratio = r
    
    def apply(self, torrents):
        for torrent in torrents:
            if torrent.status != TorrentStatus.Uploading or \
                torrent.ratio < self._ratio:
                self.remain.append(torrent)
            else:
                self.remove.append(torrent)