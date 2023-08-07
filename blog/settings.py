import os, sys
from pymongo import MongoClient


# mongo_uri = 'mongodb://' + \
#     os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]

# mongo_uri = "mongodb+srv://blog_website:dsChOS0iNKlkJULg@cluster0.o855bjo.mongodb.net/"
mongo_uri = "mongodb+srv://blogdb:ERpfVe9gUptDwt9C@cluster0.zz6st7n.mongodb.net/"
# mongo_uri = "mongodb://localhost:27017"
DB_NAME = 'blogdb'
db = MongoClient(mongo_uri)[DB_NAME]
