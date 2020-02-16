#-*- coding:utf-8 -*-

from ..compatibility.urlparse import _urlparse
from .filter import Filter

class TrackerFilter(Filter):
    def __init__(self, all_tracker, ac, re):
        Filter.__init__(self, all_tracker, ac, re)

    def apply(self, torrents):
        result = set()
        for torrent in torrents:
            for tracker in torrent.tracker: # For each tracker
                tracker = _urlparse(tracker).hostname
                if self._all or tracker in self._accept:
                    result.add(torrent)
                if tracker in self._reject:
                    result.remove(torrent)
                    break # Reject this seed
        return result