from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint
import datetime

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbEmbed"]

artistTracksCollection = db["ArtistsTracks"]
d = datetime.datetime(1950, 1, 1)


# Q4: For each track that was released after 1950-01-01,
# find the track name, artist name and track release date.

result = artistTracksCollection.aggregate([
  {
    '$unwind': {'path': '$tracks'}
  },
  {
    '$match': { 'tracks.release_date': {'$gt': d} }
  },
  {
    '$project': {'name':1, 't_name':"$tracks.name", "t_release_date":'$tracks.release_date'}
  }
])

for i in list(result):
  print(i)