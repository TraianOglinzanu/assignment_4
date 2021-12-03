from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbNorm"]

tracks_collection = db["Tracks"]

sum = 0.0
count = 0
avg = 0.0
for track in tracks_collection.find({"track_id": { "$regex": "^70"}},{"_id":1,"danceability":"$danceability"}):
  sum += float(track.get("danceability"))
  count+=1

avg = sum/count
result = {'_id':"",'avg_danceability':avg}
print(result)
