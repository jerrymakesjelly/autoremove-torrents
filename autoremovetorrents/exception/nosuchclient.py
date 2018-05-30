#-*- coding:utf-8 -*-

class NoSuchClient(RuntimeError):
    def __init__(self, arg):
        self.args = (arg,)