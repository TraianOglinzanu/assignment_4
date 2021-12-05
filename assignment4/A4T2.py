#A4T2.py

from pymongo import MongoClient
import json
from bson.json_util import loads

client = MongoClient('mongodb://127.0.0.1:27017')

#create or open database on server 
db = client["A4dbEmbed"]

# List collection names.
collist = db.list_collection_names()

if "artists" in collist:
    print("The collection exists.")

if "tracks" in collist:
    print("The collection exists.")

# Create or open the collection in the db
artists_collection = db["artists"]
tracks_collection = db["tracks"]

f = open('artists.json', encoding='utf-8')
g = open('tracks.json', encoding='utf-8')

data = loads(f.read())
data_2 = loads(g.read())

artists_collection.insert_many(data)
tracks_collection.insert_many(data_2)

ArtistsTracks = db['ArtistsTracks']

pipeline = [{
    '$lookup':{
        'from':'tracks',
        'localField': 'tracks',
        'foreignField' : 'track_id',
        'as': 'tracks'
    }
}]

for i in artists_collection.aggregate(pipeline):
    ArtistsTracks.insert_one(i)

client.drop_collection("artisits")
client.drop_collection("tracks")
