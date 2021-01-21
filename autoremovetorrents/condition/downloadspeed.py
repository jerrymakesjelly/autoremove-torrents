from .base import Comparer
from .base import Condition
from ..torrentstatus import TorrentStatus

class DownloadSpeedCondition(Condition):
    def __init__(self, downspeed, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._downspeed = downspeed
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            # Note: The speed unit is KiB/s
            # Note: This condition is only available for the downloading torrents
            if torrent.status == TorrentStatus.Downloading and self.compare(torrent.download_speed, self._downspeed * 1024, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)