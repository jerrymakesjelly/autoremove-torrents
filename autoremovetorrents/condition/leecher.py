from .base import Comparer
from .base import Condition

class LeecherCondition(Condition):
    def __init__(self, l, comp = Comparer.LT):
        Condition.__init__(self) # Initialize remain and remove list
        self._leecher = l
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.leecher, self._leecher, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)