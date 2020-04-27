# -*- coding:utf-8 -*-

from .freespacebase import FreeSpaceConditionBase
from autoremovetorrents.compatibility.disk_usage_ import disk_usage_

class FreeSpaceCondition(FreeSpaceConditionBase):
    def __init__(self, settings):
        FreeSpaceConditionBase.__init__(self, settings)
        self._path = settings['path']

    def apply(self, client_status, torrents):
        free_space = disk_usage_(self._path)['free']
        FreeSpaceConditionBase.apply(self, free_space, torrents)
