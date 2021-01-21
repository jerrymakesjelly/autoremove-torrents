from .base import Comparer
from .base import Condition
from ..torrentstatus import TorrentStatus

class ConnectedSeederCondition(Condition):
    def __init__(self, cs, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._connected_seeder = cs
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            # Note: This condition is only available for the uploading and downloading torrents
            if (torrent.status == TorrentStatus.Uploading or torrent.status == TorrentStatus.Downloading) and \
                self.compare(torrent.connected_seeder, self._connected_seeder, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)