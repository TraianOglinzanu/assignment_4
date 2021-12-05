from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbEmbed"]

tracks_collection = db["ArtistsTracks"]

# Q2: Write a query to get the average danceability for all tracks that have a track_id beginning with “70”.

sum = 0.0
count = 0
avg = 0.0
result = tracks_collection.aggregate([
    { "$unwind": '$tracks'},
    { "$match": {'tracks.track_id': {"$regex": "^70"}}},
    { "$group": {"_id": "", "avg_danceability" : {"$avg": "$tracks.danceability"}}}#why does this work
])
pprint.pprint(list(result))


# avg = sum/count
# result = {'_id':"",'avg_danceability':avg}
# print(result)
