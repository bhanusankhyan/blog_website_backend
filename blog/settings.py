import os, sys
from pymongo import MongoClient


# mongo_uri = 'mongodb://' + \
#     os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]

mongo_uri = "mongodb+srv://blog_website:dsChOS0iNKlkJULg@cluster0.o855bjo.mongodb.net/"
DB_NAME = 'blogdb'
db = MongoClient(mongo_uri)[DB_NAME]
