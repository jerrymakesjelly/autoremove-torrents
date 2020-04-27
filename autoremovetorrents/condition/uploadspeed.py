from .base import Comparer
from .base import Condition
from ..torrentstatus import TorrentStatus

class UploadSpeedCondition(Condition):
    def __init__(self, upspeed, comp = Comparer.LT):
        Condition.__init__(self) # Initialize remain and remove list
        self._upspeed = upspeed
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            # Note: The speed unit is KiB/s
            # Note: This condition is only available for the uploading torrents
            if (torrent.status == TorrentStatus.Uploading or torrent.status == TorrentStatus.Downloading) \
                and self.compare(torrent.upload_speed, self._upspeed * 1024, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)