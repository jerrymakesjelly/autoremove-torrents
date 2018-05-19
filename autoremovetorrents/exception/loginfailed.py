#-*- coding:utf-8 -*-

class LoginFailed(RuntimeError):
    def __init__(self, arg):
        self.args = arg