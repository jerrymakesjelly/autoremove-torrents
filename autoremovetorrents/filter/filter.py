#-*- coding:utf-8 -*-

class Filter(object):
    def __init__(self, all_seeds, ac, re):
        self._all = all_seeds
        self._accept = ac
        self._reject = re