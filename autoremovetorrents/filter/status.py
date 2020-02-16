from .filter import Filter
from ..torrentstatus import TorrentStatus
from .. import logger

class StatusFilter(Filter):
    def __init__(self, all_status, ac, re):
        Filter.__init__(self, all_status, ac, re)

        self._logger = logger.Logger.register(__name__) # Register a logger
        self._acc_status, self._acc_stallup, self._acc_stalldown = self._convert_status(self._accept)
        self._rej_status, self._rej_stallup, self._rej_stalldown = self._convert_status(self._reject)

    def _convert_status(self, status_list):
        result = []
        stallUp = False
        stallDown = False
        for status in status_list:
            # For StalledUploading and StalledDownloading
            if 'stalledupload' == str(status).lower():
                stallUp = True
                continue
            if 'stalleddownload' == str(status).lower():
                stallDown = True
                continue
            try:
                result.append(TorrentStatus[str(status).capitalize()])
            except KeyError:
                self._logger.warning(
                    "The status '%s' does not exist, so it won't be used."
                    % str(status)
                )
        return result, stallUp, stallDown

    def apply(self, torrents):
        result = set()

        for torrent in torrents:
            if self._all or torrent.status in self._acc_status:
                result.add(torrent)
            if self._acc_stallup and torrent.status == TorrentStatus.Uploading and torrent.stalled:
                result.add(torrent)
            if self._acc_stalldown and torrent.status == TorrentStatus.Downloading and torrent.stalled:
                result.add(torrent)
            if torrent in result and torrent.status in self._rej_status:
                result.remove(torrent)
            if torrent in result and self._rej_stallup and torrent.status == TorrentStatus.Uploading and torrent.stalled:
                result.remove(torrent)
            if torrent in result and self._rej_stalldown and torrent.status == TorrentStatus.Downloading and torrent.stalled:
                result.remove(torrent)
        
        return result