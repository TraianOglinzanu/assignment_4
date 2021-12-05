from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint
import datetime

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbEmbed"]

artistsTracksCollection = db["ArtistsTracks"]

# Q3: Find the sum of the length of all tracks for each artist along with the artist’s id.

result = artistsTracksCollection.aggregate([
  {
    '$unwind': '$tracks'
  },
  {
    '$group': {
      '_id': '$artist_id',
      'total_length': {'$sum': '$tracks.duration'}}
  },
  {
    '$project': {'total_length': 1, 'artist_id':'$_id'}
  }
])

for i in list(result):
  print(i)