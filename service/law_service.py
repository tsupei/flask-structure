# -*- coding: utf-8 -*-
import logging
from db import LawCollection


class LawService(object):
    def __init__(self, database):
        self.database = database

    def find_candicates(self, keyword, complete=True, description=True):
        law_collection = LawCollection(self.database)
        return law_collection.smart_search(keyword, complete)


