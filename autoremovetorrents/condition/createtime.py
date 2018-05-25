#-*- coding:utf-8 -*-

import time
from .base import Condition

class CreateTimeCondition(Condition):
    def __init__(self, ct):
        Condition.__init__(self) # Initialize remain and remove list
        self._create_time = ct
    
    def apply(self, torrents, now = 0):
        if now == 0:
            now = time.time()
        for torrent in torrents:
            if now - torrent.create_time <= self._create_time:
                self.remain.append(torrent)
            else:
                self.remove.append(torrent)