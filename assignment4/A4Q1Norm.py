from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint

client = MongoClient('mongodb://127.0.0.1:27017')

#create or open database on server 
db = client["A4DBNorm"]

artists_collection = db["artists"]

#important below!!!!
#right now it should return the ones that have no tracks. inverting the condition will give the right answer but thats harder to check so this is for testing

for artist in artists_collection.find({"tracks": { '$size': 0}}):
  pprint.pprint(artist)#ill figure out the correct formatting later

