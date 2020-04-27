from .base import Comparer
from .base import Condition

class ProgressCondition(Condition):
    def __init__(self, progress, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._progress = progress
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.progress, float(self._progress) / 100, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)