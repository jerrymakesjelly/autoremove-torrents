#-*- coding:utf-8 -*-

import time
from .base import Comparer
from .base import Condition

class CreateTimeCondition(Condition):
    def __init__(self, ct, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._create_time = ct
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(time.time() - torrent.create_time, self._create_time, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)