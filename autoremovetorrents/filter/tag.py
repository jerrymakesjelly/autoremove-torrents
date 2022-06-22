#-*- coding:utf-8 -*-

from .filter import Filter

class TagFilter(Filter):
    def __init__(self, all_tags, ac, re):
        Filter.__init__(self, all_tags, ac, re)

    def apply(self, torrents):
        # Pick accepted torrents
        accepts = set()
        if self._all: # Accpet all torrents (all_tags)
            accepts = set(torrents)
        elif len(self._accept) > 0: # Accept specific tag torrents (tags)
            for torrent in torrents:
                for tag in torrent.tags:
                    if tag in self._accept:
                        accepts.add(torrent)
        # Pick rejected torrents
        rejects = set()
        if len(self._reject) > 0: # Reject specific tag torrents (excluded_tags)
            for torrent in accepts:
                for tag in torrent.tags:
                    if tag in self._reject:
                        rejects.add(torrent)
        return accepts.difference(rejects) # Return their difference