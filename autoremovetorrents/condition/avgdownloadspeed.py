from .base import Comparer
from .base import Condition

class AverageDownloadSpeedCondition(Condition):
    def __init__(self, avg_dl_speed, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._avg_dl_speed = avg_dl_speed # In KiB
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.average_download_speed, self._avg_dl_speed * 1024, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)