from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbNorm"]

artists = db["Artists"]

# Q3: Find the sum of the length of all tracks for each artist along with the artist’s id.

result = artists.aggregate([
  {
    '$lookup': {
        'from':'Tracks',
        'localField': 'tracks',
        'foreignField' : 'track_id',
        'as': 'tracks'
    }
  },
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