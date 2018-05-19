#-*- coding:utf-8 -*-

from .base import Condition

class ConditionWithSort(Condition):
    def __init__(self, action):
        Condition.__init__(self)
        self._action = action
    
    def sort_torrents(self, torrents):
        actions = [
            'remove-old-seeds',
            'remove-new-seeds',
            'remove-big-seeds',
            'remove-small-seeds'
        ]
        parameter = [
            {'key':lambda torrent: torrent.create_time, 'reverse':True},
            {'key':lambda torrent: torrent.create_time, 'reverse':False},
            {'key':lambda torrent: torrent.size, 'reverse':False},
            {'key':lambda torrent: torrent.size, 'reverse':True}
        ]
        for i in range(0, len(actions)):
            if self._action == actions[i]:
                torrents.sort(key=parameter[i]['key'], reverse=parameter[i]['reverse'])