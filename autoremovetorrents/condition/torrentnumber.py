from .sortbase import ConditionWithSort

class TorrentNumberCondition(ConditionWithSort):
    def __init__(self, settings):
        ConditionWithSort.__init__(self, settings['action'])
        self._max_limit = settings['limit']

    def apply(self, client_status, torrents):
        torrents = list(torrents)
        ConditionWithSort.sort_torrents(self, torrents)
        if self._max_limit == 0:
            self.remove = torrents
        elif self._max_limit < len(torrents):
            self.remove = set(torrents[0:len(torrents)-self._max_limit])
            self.remain = set(torrents[len(torrents)-self._max_limit:])
        else:
            self.remain = torrents