#A4T1.py

from pymongo import MongoClient
import json
from bson.json_util import loads

client = MongoClient('mongodb://127.0.0.1:27017')

#create or open database on server 
db = client["A4DBNorm"]

# List collection names.
collist = db.list_collection_names()

if "artists" in collist:
    print("The collection exists.")

if "tracks" in collist:
    print("The collection exists.")

# Create or open the collection in the db
artists_collection = db["artists"]
tracks_collection = db["tracks"]

f = open('artists.json')
g = open('tracks.json')

data = loads(f.read())
data_2 = loads(g.read())

artists_collection.insert_many(data)
tracks_collection.insert_many(data_2)




