#-*- coding:utf-8 -*-

from .base import Condition

class EmptyCondition(Condition):
    def __init__(self, any_data):
        Condition.__init__(self)

    def apply(self, client_status, torrents):
        self.remain = torrents