from .base import Comparer
from .base import Condition

class AverageUploadSpeedCondition(Condition):
    def __init__(self, avg_ul_speed, comp = Comparer.LT):
        Condition.__init__(self) # Initialize remain and remove list
        self._avg_ul_speed = avg_ul_speed # In KiB
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(torrent.average_upload_speed, self._avg_ul_speed * 1024, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)