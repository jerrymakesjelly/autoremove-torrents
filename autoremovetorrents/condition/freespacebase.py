from .sortbase import ConditionWithSort

# FreeSpaceConditionBase:
# Implements basic deletion logic via free space
class FreeSpaceConditionBase(ConditionWithSort):
    def __init__(self, settings):
        ConditionWithSort.__init__(self, settings['action'])
        self._min = settings['min'] << 30 # Convert B to GiB

    def apply(self, free_space, torrents):
        torrents = list(torrents)
        ConditionWithSort.sort_torrents(self, torrents)
        for torrent in torrents:
            if free_space < self._min:
                free_space += torrent.size
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)
