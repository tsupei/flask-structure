import pymongo
import abc
import logging

logger = logging.getLogger("autocomplete")

class MongoCollection(abc.ABC):
    def __init__(self):
        self.collection_name = self.get_collection_name()

    @abc.abstractclassmethod
    def get_collection_name(self):
        return NotImplementedError("Error! collection name is not specified!")


class QuoteCollection(MongoCollection):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.collection = db[self.collection_name]

    def get_collection_name(self):
        return "quotes"

    def search(self, keyword, complete):
        quotes = list(self.collection.find({
            "quote": {
                '$regex': '^{}.*'.format(keyword)
            }
        }))
        print(quotes)
        match = set()
        for quote in quotes:
            match.add(quote["quote"])
        match = list(match)
        if not complete:
            match = [quote[len(keyword):] for quote in match]
            match = filter(lambda x:x, match)
        logger.debug("match: {}".format(match))
        return sorted(match, key=lambda k: len(k))

class LawCollection(MongoCollection):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.collection = db[self.collection_name]

    def get_collection_name(self):
        return "law"

    def search(self, keyword, complete, description):
        laws = list(self.collection.find({
            "name": {
                    '$regex': '^{}.*'.format(keyword)
            }
        }))
        match = []
        for law in laws:
            match.append({
                "name": law["name"],
                "description": law["description"]
            })
        if not complete:
            match = [{"name": law["name"][len(keyword):], "description": law["description"]} for law in match]
            match = filter(lambda x:x["name"], match)
        logger.debug("match: {}".format(match))
        return sorted(match, key=lambda k: (len(k["name"]), k["name"]))

class OpinionCollection(MongoCollection):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.collection = db[self.collection_name]

    def get_collection_name(self):
        return "opinion"

    def search(self, keyword, complete):
        opinions = list(self.collection.find({
                "concept": {
                    '$regex': '{}.*'.format(keyword)
                }
            }))
        valid_concept = {}
        for opinion in opinions:
            if opinion["concept"] not in valid_concept:
                valid_concept[opinion["concept"]] = [opinion["description"]]
            else:
                valid_concept[opinion["concept"]].append(opinion["description"])
        match = []
        for key, value in valid_concept.items():
            if not value:
                continue
            match.append({
                "concept": key if complete else key[len(keyword):],
                "descriptions": value,
                "count": len(value) 
            })
        return match

