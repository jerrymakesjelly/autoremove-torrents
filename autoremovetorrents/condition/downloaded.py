from .base import Comparer
from .base import Condition

class DownloadsCondition(Condition):
    def __init__(self, downloads, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._downloads = downloads << 30 # Convert bytes to GiB
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.downloaded, self._downloads, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)
