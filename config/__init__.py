import logging
import os
import ahocorasick
from flask import current_app
from pymongo import MongoClient

# Read yaml settings

def init():
    # Initialize MongoDB
    mongo_client = MongoClient(host="localhost", port=27017)
    database = mongo_client['DrinkBot']
    current_app.config['database'] = database

    # Initialize Automaton
    automaton = _init_automaton(database)
    current_app.config["automaton"] = automaton

def _init_automaton(db):
    automaton = ahocorasick.Automaton()

    # Pull down drink data from db
    collection = db['drink']
    drinks = list(collection.find())
    for drink in drinks:
        automaton.add_word(drink["name"], ("drink", drink["name"]))

    # Pull down ice data from db
    collection = db['ice']
    ices = list(collection.find())
    for ice in ices:
        automaton.add_word(ice["name"], ("ice", ice["name"]))

    # Pull down sugar data from db
    collection = db['sugar']
    sugars = list(collection.find())
    for sugar in sugars:
        automaton.add_word(sugar["name"], ("sugar", sugar["name"]))

    # Pull down topping data from db
    automaton.make_automaton()
    return automaton

# Initialization: Mongodb, ...
