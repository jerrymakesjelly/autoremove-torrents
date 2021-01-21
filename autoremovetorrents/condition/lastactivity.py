import time
from .base import Comparer
from .base import Condition

class LastActivityCondition(Condition):
    def __init__(self, la, comp = Comparer.GT):
        Condition.__init__(self)
        self._last_activity = la
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(time.time() - torrent.last_activity, self._last_activity, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)