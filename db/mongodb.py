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

    def smart_search(self, sent, complete):
        # At most trace back to ten characters
        sent = sent[-10:]
        quotes = list(self.collection.find())

        cur_text = ""
        best_res = []
        i = 0
        while i < len(sent):
            char = sent[i]
            cur_text += char
            match = set()
            print(char, cur_text)
            for quote in quotes:
                if quote["quote"].startswith(cur_text):
                    match.add(quote["quote"])
            if match:
                best_res = list(match)
                i += 1
            else:
                if len(cur_text) == 1:
                    i += 1
                cur_text = ""
        if not complete:
            best_res = [quote[len(keyword):] for quote in best_res]
            best_res = filter(lambda x:x, best_res)
        return cur_text, sorted(best_res, key=lambda  k: len(k))

    def search(self, keyword, complete):
        quotes = list(self.collection.find({
            "quote": {
                '$regex': '^{}.*'.format(keyword)
            }
        }))
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

    def smart_search(self, sent, complete):
        # At most trace back to ten characters
        sent = sent[-10:]
        laws = list(self.collection.find())

        cur_text = ""
        best_res = []
        i = 0
        while i < len(sent):
            char = sent[i]
            cur_text += char
            match = []
            for law in laws:
                if law["name"].startswith(cur_text):
                    match.append({
                        "name": law["name"],
                        "description": law["description"]
                    })
            if match:
                best_res = match
                i += 1
            else:
                if len(cur_text) == 1:
                    i += 1
                cur_text = ""
        if not complete:
            best_res = [law[len(keyword):] for law in best_res]
            best_res = filter(lambda x:x, best_res)
        return cur_text, sorted(best_res, key=lambda  k: len(k))

    def search(self, keyword, complete):
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

    def smart_search(self, sent, complete):
        # At most trace back to ten characters
        sent = sent[-10:]
        opinions = list(self.collection.find())

        cur_text = ""
        best_res = []
        i = 0
        while i < len(sent):
            cur_text += char
            match = []
            valid_concept = {}
            for opinion in opinions:
                if opinion["concept"].startswith(cur_text):
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
            if match:
                best_res = match
                i += 1
            else:
                if len(cur_text) == 1:
                    i += 1
                cur_text = ""
        return cur_text, match

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

