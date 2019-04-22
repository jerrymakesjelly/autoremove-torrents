#-*- coding:utf-8 -*-

import time
from .base import Comparer
from .base import Condition

class CreateTimeCondition(Condition):
    def __init__(self, ct, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._create_time = ct
        self._comparer = comp

    def apply(self, torrents, now = 0):
        # In order to test this condition, let's make something different
        if isinstance(self._create_time, dict) and 'timestamp' in self._create_time:
            now = self._create_time['timestamp']
            self._create_time = self._create_time['value']
        else:
            now = time.time()
        # Execute
        for torrent in torrents:
            if self.compare(now - torrent.create_time, self._create_time, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)