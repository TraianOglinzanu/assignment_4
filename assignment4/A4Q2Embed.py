from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbEmbed"]

tracks_collection = db["ArtistsTracks"]

sum = 0.0
count = 0
avg = 0.0
# for track in tracks_collection.find({"tracks.track_id": { "$regex": "^70"}},{"_id":"$tracks.track_id","danceability":"$tracks.danceability"}):
#   pprint.pprint(track)
result = tracks_collection.aggregate([
    { "$unwind": '$tracks'},
    { "$match": {'tracks.track_id': {"$regex": "^70"}}},
    { "$group": {"_id": "", "avg_danceability" : {"$avg": "$tracks.danceability"}}}#why does this work
])
pprint.pprint(list(result))


# avg = sum/count
# result = {'_id':"",'avg_danceability':avg}
# print(result)
