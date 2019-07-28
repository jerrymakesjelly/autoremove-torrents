from .base import Comparer
from .base import Condition

class ConnectedSeederCondition(Condition):
    def __init__(self, cs, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._connected_seeder = cs
        self._comparer = comp
    
    def apply(self, torrents):
        for torrent in torrents:
            if self.compare(torrent.connected_seeder, self._connected_seeder, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)