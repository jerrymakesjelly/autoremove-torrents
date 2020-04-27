from .base import Comparer
from .base import Condition

class SeederCondition(Condition):
    def __init__(self, s, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._seeder = s
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.seeder, self._seeder, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)