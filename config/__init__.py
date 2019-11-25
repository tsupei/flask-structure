import logging
import os
from flask import current_app
from pymongo import MongoClient

# Read yaml settings


# Initialization: Mongodb, ...
def init_db():
    mongo_client = MongoClient(host="localhost", port=27017)
    database = mongo_client['LawPilot']
    current_app.config['database'] = database
