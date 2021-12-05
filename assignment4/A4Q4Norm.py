from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbNorm"]

tracks_collection = db["Tracks"]
d = datetime.datetime(1950, 1, 1)


# Q4: For each track that was released after 1950-01-01,
# find the track name, artist name and track release date.

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