#-*- coding:utf-8 -*-

from .filter import Filter

class PathFilter(Filter):
    def __init__(self, all_paths, ac, re):
        '''filter torrents by path (download directory)

        Parameters:
          all_paths (boolean): whether accept all paths
          ac (list): accept paths
          re (list): reject paths
        '''
        Filter.__init__(self, all_paths, ac, re)

    def apply(self, torrents):
        # Pick accepted torrents
        accepts = set()
        if self._all: # Accept all torrents (all_paths)
            accepts = set(torrents)
        elif len(self._accept) > 0: # Accept specific path torrents (paths)
            for torrent in torrents:
                path = torrent.download_dir
                if path in self._accept or path == '':
                    accepts.add(torrent)
        # Pick rejected torrents
        rejects = set()
        if len(self._reject) > 0: # Reject specific path torrents (excluded_paths)
            for torrent in accepts:
                path = torrent.download_dir
                if path in self._reject:
                    rejects.add(torrent)
        return accepts.difference(rejects) # Return their difference