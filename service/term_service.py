# -*- coding: utf-8 -*-
import logging
from db import QuoteCollection


class TermService(object):
    def __init__(self, database):
        self.database = database

    def find_candicates(self, keyword, complete=True):
        quote_collection = QuoteCollection(self.database)
        return quote_collection.smart_search(keyword, complete)


