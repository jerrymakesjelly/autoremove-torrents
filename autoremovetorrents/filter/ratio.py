#-*- coding:utf-8 -*-

from .filter import Filter
from .. import logger

class RatioFilter(Filter):
    def __init__(self, min_ratio=None, max_ratio=None):
        super(RatioFilter, self).__init__(all_seeds=None, ac=None, re=None)
        # ADDED: Initialize logger
        self._logger = logger.Logger.register(__name__)
        # Convert to float, handling None by setting to 0.0 for min and inf for max
        self._min_ratio = float(min_ratio) if min_ratio is not None else 0.0
        self._max_ratio = float(max_ratio) if max_ratio is not None else float('inf')

        # It's a good practice to ensure min_ratio is not greater than max_ratio.
        # If min_ratio > max_ratio, it would result in no torrents passing the filter.
        if self._min_ratio > self._max_ratio:
            self._logger.warning(
                f"min_ratio ({self._min_ratio}) is greater than max_ratio ({self._max_ratio}). "
                f"This will result in no torrents passing this filter."
            )

    def apply(self, torrents):
        # If min_ratio is at its effective minimum (0.0) and max_ratio is at its effective maximum (infinity),
        # it means no specific filtering range is specified by the user for ratios,
        # so all torrents pass this filter.
        if self._min_ratio == 0.0 and self._max_ratio == float('inf'):
            return set(torrents)

        filtered_torrents = set()
        for torrent in torrents:
            ratio = torrent.ratio # Assuming torrent.ratio provides the numerical ratio

            effective_ratio = 0.0 # Default for problematic or non-numeric ratios
            if isinstance(ratio, (int, float)):
                if ratio < 0: # Handle special values like -1 (e.g., qBittorrent's infinity)
                    effective_ratio = float('inf')
                else:
                    effective_ratio = float(ratio) # Ensure it's a float for comparison
            else:
                # For non-numeric ratios, effective_ratio remains 0.0.
                torrent_name = getattr(torrent, 'name', 'N/A') # Safely get torrent name
                self._logger.warning(f"Torrent '{torrent_name}' has a non-numeric ratio: {ratio}. Treating as 0.0 for filtering.")

            if self._min_ratio <= effective_ratio <= self._max_ratio:
                filtered_torrents.add(torrent)
        return filtered_torrents

