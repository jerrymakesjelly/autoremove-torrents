from .base import Comparer
from .base import Condition

class SizeCondition(Condition):
    def __init__(self, s, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._size = s * (1 << 30) # Convert to GiB
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.size, self._size, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)