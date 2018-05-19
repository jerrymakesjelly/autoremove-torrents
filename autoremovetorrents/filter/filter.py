#-*- coding:utf-8 -*-

class Filter(object):
    def __init__(self, all, ac, re):
        self._all = all
        self._accept = ac
        self._reject = re