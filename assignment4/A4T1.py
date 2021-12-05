#A4T1.py

from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient('mongodb://127.0.0.1:27017')

#create or open database on server 
db = client["A4dbNorm"]

# List collection names.
collist = db.list_collection_names()

if "Artists" in collist:
    print("The collection exists.")

if "Tracks" in collist:
    print("The collection exists.")

# Create or open the collection in the db
artists_collection = db["Artists"]
tracks_collection = db["Tracks"]

f = open('artists.json', encoding='utf-8')
g = open('tracks.json', encoding='utf-8')

data = loads(f.read())
data_2 = loads(g.read())

artists_collection.insert_many(data)
tracks_collection.insert_many(data_2)




