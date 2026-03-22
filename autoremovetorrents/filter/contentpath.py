#-*- coding:utf-8 -*-

from .filter import Filter
import os
import fnmatch

class ContentPathFilter(Filter):
    """
    Filter torrents by their content path (download directory).
    
    Supports:
    - Exact path match: '/downloads/movies'
    - Glob patterns: '/downloads/*'
    - Multiple paths: accept ['/downloads/movies', '/downloads/tv']
    
    Config example:
      content_paths:
        - /downloads/movies
        - /downloads/tv/*
      excluded_content_paths:
        - /downloads/important
    """
    def __init__(self, all_content_paths, ac, re):
        Filter.__init__(self, all_content_paths, ac, re)

    def _match_path(self, torrent_path, patterns):
        """Check if torrent path matches any of the patterns."""
        if not hasattr(torrent_path, '__len__'):
            torrent_path = [torrent_path] if torrent_path else []
        
        for pattern in patterns:
            # Normalize paths for comparison
            normalized_pattern = os.path.normpath(pattern)
            for tp in (torrent_path if isinstance(torrent_path, list) else [torrent_path]):
                if tp is None:
                    continue
                normalized_tp = os.path.normpath(tp)
                
                # Exact match
                if normalized_tp == normalized_pattern:
                    return True
                
                # Glob pattern match
                if fnmatch.fnmatch(normalized_tp, normalized_pattern):
                    return True
                
                # Check if pattern is a parent directory
                if normalized_tp.startswith(normalized_pattern + os.sep):
                    return True
                
                # Wildcard matching for patterns ending with /*
                if pattern.endswith('/*'):
                    parent = os.path.normpath(pattern[:-2])
                    if normalized_tp.startswith(parent + os.sep):
                        return True
        
        return False

    def apply(self, torrents):
        # Pick accepted torrents
        accepts = set()
        if self._all:  # Accept all torrents (all_content_paths)
            accepts = set(torrents)
        elif len(self._accept) > 0:  # Accept specific content path torrents
            for torrent in torrents:
                if not hasattr(torrent, 'content_path') or torrent.content_path is None:
                    # If content_path not available, skip this torrent
                    continue
                if self._match_path(torrent.content_path, self._accept):
                    accepts.add(torrent)
        
        # Pick rejected torrents
        rejects = set()
        if len(self._reject) > 0:  # Reject specific content path torrents
            for torrent in accepts:
                if not hasattr(torrent, 'content_path') or torrent.content_path is None:
                    continue
                if self._match_path(torrent.content_path, self._reject):
                    rejects.add(torrent)
        
        return accepts.difference(rejects)