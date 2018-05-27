from .filter import Filter
from ..torrentstatus import TorrentStatus
from .. import logger

class StatusFilter(Filter):
    def __init__(self, all_status, ac, re):
        Filter.__init__(self, all_status, ac, re)
        self._logger = logger.register(__name__) # Register a logger

    def _convert_status(self, status_list):
        result = []
        for status in status_list:
            try:
                result.append(TorrentStatus[str(status).capitalize()])
            except KeyError:
                self._logger.warning(
                    "The status '%s' does not exist, so it won't be used."
                    % str(status)
                )
        return result
    
    def apply(self, torrents):
        # Generate accpet and reject lists
        accept = self._convert_status(self._accept)
        reject = self._convert_status(self._reject)

        return [torrent for torrent in torrents 
            if (self._all or torrent.status in accept)
            and not (torrent.status in reject)
        ]