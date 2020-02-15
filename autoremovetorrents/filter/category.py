#-*- coding:utf-8 -*-

from .filter import Filter

class CategoryFilter(Filter):
    def __init__(self, all_category, ac, re):
        Filter.__init__(self, all_category, ac, re)

    def apply(self, torrents):
        result = set()
        if self._all:
            result = torrents
        else:
            for torrent in torrents:
                for category in torrent.category: # For each category
                    if category in self._accept:
                        result.add(torrent)
                    if category in self._reject:
                        result.remove(torrent)
                        break # Reject this seed
        return result