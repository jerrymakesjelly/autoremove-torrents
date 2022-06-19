#-*- coding:utf-8 -*-

from .base import Condition
from autoremovetorrents.compatibility.inf_ import inf_

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
            # For remove-active-seeds and remove-inactive-seeds,
            # we move the torrents that are never active to the bottom of the list,
            # to remove as many active torrents as possible.
            'remove-active-seeds': {'key':
                lambda torrent: torrent.last_activity if torrent.last_activity is not None else inf_,
            'reverse':False},
            'remove-inactive-seeds': {'key':
                lambda torrent: torrent.last_activity if torrent.last_activity is not None else -inf_,
            'reverse':True},
            'remove-slow-upload-seeds': {'key':lambda torrent: torrent.upload_speed, 'reverse':False},
            'remove-fast-upload-seeds': {'key':lambda torrent: torrent.upload_speed, 'reverse':True}
        }
        if self._action in handlers.keys():
            torrents.sort(key=handlers[self._action]['key'], reverse=handlers[self._action]['reverse'])
