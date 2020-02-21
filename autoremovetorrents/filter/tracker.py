#-*- coding:utf-8 -*-

from ..compatibility.urlparse_ import urlparse_
from .filter import Filter

class TrackerFilter(Filter):
    def __init__(self, all_tracker, ac, re):
        Filter.__init__(self, all_tracker, ac, re)

    def apply(self, torrents):
        # Pick accepted torrents
        accepts = set()
        if self._all: # Accpet all torrents (all_trackers)
            accepts = set(torrents)
        elif len(self._accept) > 0: # Accept specific tracker torrents (trackers)
            for torrent in torrents:
                for tracker in torrent.tracker:
                    hostname = urlparse_(tracker).hostname
                    if hostname in self._accept or tracker in self._accept:
                        accepts.add(torrent)
        # Pick rejected torrents
        rejects = set()
        if len(self._reject) > 0: # Reject specific tracker torrents (excluded_trackers)
            for torrent in accepts:
                for tracker in torrent.tracker:
                    hostname = urlparse_(tracker).hostname
                    if hostname in self._reject or tracker in self._reject:
                        rejects.add(torrent)
        return accepts.difference(rejects) # Return their difference