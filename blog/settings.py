import os, sys
from pymongo import MongoClient

mongo_uri = "mongodb+srv://blogdb:ERpfVe9gUptDwt9C@cluster0.kbuanl1.mongodb.net/"
# mongo_uri = "mongodb://localhost:27017"
DB_NAME = 'blogdb'
db = MongoClient(mongo_uri)[DB_NAME]
