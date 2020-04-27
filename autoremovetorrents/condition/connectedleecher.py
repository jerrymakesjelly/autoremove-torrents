from .base import Comparer
from .base import Condition
from ..torrentstatus import TorrentStatus

class ConnectedLeecherCondition(Condition):
    def __init__(self, cl, comp = Comparer.LT):
        Condition.__init__(self) # Initialize remain and remove list
        self._connected_leecher = cl
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            # Note: This condition is only available for the uploading and the downloading torrents
            if (torrent.status == TorrentStatus.Downloading or torrent.status == TorrentStatus.Uploading) \
                and self.compare(torrent.connected_leecher, self._connected_leecher, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)