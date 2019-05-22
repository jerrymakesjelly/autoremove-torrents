#-*- coding:utf-8 -*-

from .filter import Filter

class CategoryFilter(Filter):
    def __init__(self, all_category, ac, re):
        Filter.__init__(self, all_category, ac, re)

    def apply(self, torrents):
        return set([torrent for torrent in torrents if (self._all or torrent.category in self._accept)
            and not (torrent.category in self._reject)])