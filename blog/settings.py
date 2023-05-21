import os, sys
from pymongo import MongoClient


# mongo_uri = 'mongodb://' + \
#     os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]

mongo_uri = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
DB_NAME = 'blogdb'
db = MongoClient(mongo_uri)[DB_NAME]
