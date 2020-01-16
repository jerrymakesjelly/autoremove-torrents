#-*- coding:utf-8 -*-

from .base import Condition

class ConditionWithSort(Condition):
    def __init__(self, action):
        Condition.__init__(self)
        self._action = action

    def sort_torrents(self, torrents):
        handlers = {
            'remove-old-seeds': {'key':lambda torrent: torrent.create_time, 'reverse':False},
            'remove-new-seeds': {'key':lambda torrent: torrent.create_time, 'reverse':True},
            'remove-big-seeds': {'key':lambda torrent: torrent.size, 'reverse':True},
            'remove-small-seeds': {'key':lambda torrent: torrent.size, 'reverse':False},
            'remove-active-seeds': {'key':lambda torrent: torrent.last_activity, 'reverse':True},
            'remove-inactive-seeds': {'key':lambda torrent: torrent.last_activity, 'reverse':False}
        }
        if self._action in handlers.keys():
            torrents.sort(key=handlers[self._action]['key'], reverse=handlers[self._action]['reverse'])