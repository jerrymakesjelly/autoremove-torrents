#-*- coding:utf-8 -*-

from .filter import Filter

class TagFilter(Filter):
    def __init__(self, all_tag, ac, re):
        Filter.__init__(self, all_category, ac, re)

    def apply(self, torrents):
        # Pick accepted torrents
        accepts = set()
        if self._all: # Accpet all torrents (all_tags)
            accepts = set(torrents)
        elif len(self._accept) > 0: # Accept specific tags torrents (tags)
            for torrent in torrents:
                for tag in torrent.tag:
                    if tag in self._accept:
                        accepts.add(torrent)
        # Pick rejected torrents
        rejects = set()
        if len(self._reject) > 0: # Reject specific tags torrents (excluded_tags)
            for torrent in accepts:
                for category in torrent.tag:
                    if category in self._reject:
                        rejects.add(torrent)
        return accepts.difference(rejects) # Return their difference
