from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint

client = MongoClient('mongodb://127.0.0.1:27017')

#create or open database on server 
db = client["A4DBNorm"]

tracks_collection = db["Tracks"]

for tracks in tracks_collection.find({"track_id": "/70/"}):#<<should work or fail horribly not sure
  pprint.pprint(tracks)#ill figure out the correct formatting later

