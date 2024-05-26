# -*- coding:utf-8 -*-

class Filter(object):
    def __init__(self, all_seeds, ac, re):
        self._all = all_seeds
        self._accept = set(ac)
        self._reject = set(re)

    def __str__(self):
        return f"Filter(all_seeds={self._all}, accept={self._accept}, reject={self._reject})"
