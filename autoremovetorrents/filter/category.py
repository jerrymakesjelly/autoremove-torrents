from .filter import Filter

class CategoryFilter(Filter):
    def __init__(self, all_categories, ac, re):
        Filter.__init__(self, all_categories, ac, re)
    
    def apply(self, torrents):
        # Please note that, if the excluded_categories is configured,
        # it will always take effect even if the all_categories is configured.
        if self._all and len(self._reject) == 0:
            return set(torrents) # For all_categories

        result = set()
        
        for torrent in torrents:
            if (self._all or torrent.category in self._accept) \
                    and torrent.category not in self._reject:
                result.add(torrent)
        
        return result
