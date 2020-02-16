#-*- coding:utf-8 -*-

from .filter import Filter

class CategoryFilter(Filter):
    def __init__(self, all_category, ac, re):
        Filter.__init__(self, all_category, ac, re)

    def apply(self, torrents):
        result = set()
        for torrent in torrents:
            for category in torrent.category: # For each category
                if self._all or category in self._accept:
                    result.add(torrent)
                if category in self._reject:
                    result.remove(torrent)
                    break # Reject this seed
        return result