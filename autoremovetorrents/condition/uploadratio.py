from .base import Comparer
from .base import Condition

class UploadRatioCondition(Condition):
    '''Upload Ratio refers to the ratio of uploaded size to file size'''

    def __init__(self, ratio, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._ratio = ratio
        self._comparer = comp

    def apply(self, client_status, torrents):
        for torrent in torrents:
            if self.compare(float(torrent.uploaded)/float(torrent.size), self._ratio, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)