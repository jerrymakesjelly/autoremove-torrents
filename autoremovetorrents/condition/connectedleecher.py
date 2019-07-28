from .base import Comparer
from .base import Condition

class ConnectedLeecherCondition(Condition):
    def __init__(self, cl, comp = Comparer.LT):
        Condition.__init__(self) # Initialize remain and remove list
        self._connected_leecher = cl
        self._comparer = comp
    
    def apply(self, torrents):
        for torrent in torrents:
            if self.compare(torrent.connected_leecher, self._connected_leecher, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)