#-*- coding:utf-8 -*-

try: # for Python 3
    from urllib.parse import urlparse
except ImportError: # for Python 2.7
    from urlparse import urlparse

from .filter import Filter

class TrackerFilter(Filter):
    def __init__(self, all_tracker, ac, re):
        Filter.__init__(self, all_tracker, ac, re)

    def apply(self, torrents):
        result = set()
        for torrent in torrents:
            for tracker in torrent.tracker: # For each tracker
                tracker = urlparse(tracker).hostname
                if self._all or tracker in self._accept:
                    if torrent not in result:
                        result.add(torrent)
                if tracker in self._reject:
                    result.remove(torrent)
                    break # Reject this seed
        return result