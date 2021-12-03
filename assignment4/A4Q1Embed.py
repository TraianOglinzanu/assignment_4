from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbEmbed"]

artists_collection = db["ArtistsTracks"]

for artist in artists_collection.find({"$where": "this.tracks.length > 1"}, {"artist_id":1, "name":1,"num":"$tracks"}):
  artist["num"] = len(artist.get("num"))
  print(artist)
