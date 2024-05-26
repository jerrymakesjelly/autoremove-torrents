# -*- coding:utf-8 -*-

from .filter import Filter

class TagFilter(Filter):
    def __init__(self, all_tags, ac, re):
        super().__init__(all_tags, ac, re)

    def apply(self, torrents):
        # Debugging: Print the tags for each torrent
        # for torrent in torrents:
        #     print(f"Torrent: {torrent.name}, Tags: {torrent.tags}")

        # Pick accepted torrents
        accepts = set()
        if self._all:
            accepts = set(torrents)
        elif len(self._accept) > 0:
            for torrent in torrents:
                for tag in torrent.tags:
                    if tag in self._accept:
                        accepts.add(torrent)

        # Pick rejected torrents
        rejects = set()
        if len(self._reject) > 0:
            for torrent in accepts:
                for tag in torrent.tags:
                    if tag in self._reject:
                        rejects.add(torrent)

        result = accepts.difference(rejects)
        return result
