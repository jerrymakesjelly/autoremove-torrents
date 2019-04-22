#-*- coding:utf-8 -*-
from enum import Enum

Comparer = Enum('Comparer', ('LT', 'GT'))

class Condition(object):
    def __init__(self):
        # Results
        self.remain = set()
        self.remove = set()
    
    def compare(self, a, b, comp):
        return (comp == Comparer.LT and a < b) or (comp == Comparer.GT and a > b)