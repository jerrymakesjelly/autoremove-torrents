#-*- coding:utf-8 -*-

class LoginFailure(RuntimeError):
    def __init__(self, arg):
        self.args = (arg,)