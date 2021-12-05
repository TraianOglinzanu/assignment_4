from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint
import datetime

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbNorm"]

tracks_collection = db["Tracks"]
d = datetime.datetime(1950, 1, 1)


from pymongo import MongoClient
import json
from bson.json_util import loads
import pprint
import datetime

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbNorm"]

tracks_collection = db["Tracks"]
d = datetime.datetime(1950, 1, 1)


# Q3: Find the sum of the length of all tracks for each artist along with the artist’s id.

result = tracks_collection.aggregate([
  {
    '$match': { 'release_date': {'$gt': d} }
  },
  {
    '$lookup': {
        'from':'Artists',
        'localField': 'artist_ids',
        'foreignField' : 'artist_id',
        'as': 'artists'
    }
  },
  {
    '$project': {'name':'$artists.name', 't_name':"$name", "t_release_date":'$release_date'}
  }
])

for i in list(result):
  print(i)

result = tracks_collection.aggregate([
  {
    '$match': { 'release_date': {'$gt': d} }
  },
  {
    '$lookup': {
        'from':'Artists',
        'localField': 'artist_ids',
        'foreignField' : 'artist_id',
        'as': 'artists'
    }
  },
  {
    '$project': {'name':'$artists.name', 't_name':"$name", "t_release_date":'$release_date'}
  }
])

for i in list(result):
  print(i)