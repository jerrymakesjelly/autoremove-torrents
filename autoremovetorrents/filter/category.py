#-*- coding:utf-8 -*-

from .filter import Filter

class CategoryFilter(Filter):
    def __init__(self, all_category, ac, re):
        Filter.__init__(self, all_category, ac, re)

    def apply(self, torrents):
        # Pick accepted torrents
        accepts = set()
        if self._all: # Accpet all torrents (all_categories)
            accepts = set(torrents)
        elif len(self._accept) > 0: # Accept specific category torrents (categories)
            for torrent in torrents:
                for category in torrent.category:
                    if category in self._accept:
                        accepts.add(torrent)
        # Pick rejected torrents
        rejects = set()
        if len(self._reject) > 0: # Reject specific category torrents (excluded_categories)
            for torrent in accepts:
                for category in torrent.category:
                    if category in self._reject:
                        rejects.add(torrent)
        return accepts.difference(rejects) # Return their difference