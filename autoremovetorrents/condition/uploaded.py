from .base import Comparer
from .base import Condition

class UploadsCondition(Condition):
    def __init__(self, uploads, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._uploads = uploads << 30 # Convert bytes to GiB
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.uploaded, self._uploads, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)
