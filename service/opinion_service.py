# -*- coding: utf-8 -*-
import logging
from db import OpinionCollection


class OpinionService(object):
    def __init__(self, database):
        self.database = database

    def find_candicates(self, keyword, complete=True):
        opinion_collection = OpinionCollection(self.database)
        return opinion_collection.search(keyword, complete)


