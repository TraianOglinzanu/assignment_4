from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint
import datetime

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbNorm"]

tracks_collection = db["Tracks"]
d = datetime.datetime(1950, 1, 1)

# not complete
for track in tracks_collection.find({'release_date': {'$gt': d}}, {"name":1, "artist_ids":1, "release_date":1}):
  print(track)

