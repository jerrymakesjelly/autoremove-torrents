from .filter import Filter
from ..torrentstatus import TorrentStatus
from .. import logger

class StatusFilter(Filter):
    def __init__(self, all_status, ac, re):
        Filter.__init__(self, all_status, ac, re)

        self._logger = logger.Logger.register(__name__) # Register a logger
        self._acc_status = self._convert_status(self._accept)
        self._rej_status = self._convert_status(self._reject)

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
        return set([torrent for torrent in torrents 
            if (self._all or torrent.status in self._acc_status)
            and not (torrent.status in self._rej_status)
        ])