from .base import Comparer
from .base import Condition

class LastActivityCondition(Condition):
    def __init__(self, la, comp = Comparer.GT):
        Condition.__init__(self)
        self._last_activity = la
        self._comparer = comp

        # If users set
        #   last_activity: Never
        # or
        #   last_activity: None,
        # we use a different function to check the torrents' activity

        self._executor = self._apply_to_never_active_torrents \
            if isinstance(la, str) and la.lower() in ['never', 'none'] else \
            self._apply_to_ever_active_torrents

    def apply(self, client_status, torrents):
        self._executor(client_status, torrents)

    # Process the torrents that are ever active
    def _apply_to_ever_active_torrents(self, client_status, torrents):
        for torrent in torrents:
            if torrent.last_activity is not None \
                and self.compare(torrent.last_activity, self._last_activity, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)

    # Process the torrents that are never active
    def _apply_to_never_active_torrents(self, client_status, torrents):
        for torrent in torrents:
            if torrent.last_activity is None:
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)