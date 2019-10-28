# -*- coding: utf-8 -*-
import logging


class HelloService(object):
    def __init__(self):
        pass

    def hello(self, user_id):
        return "hello! {}".format(user_id)


