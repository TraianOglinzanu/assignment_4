from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

#create or open database on server 
db = client["A4dbEmbed"]

artists_collection = db["ArtistsTracks"]

# Q1: Find the ids and names of each artist that has at least one track and the number of tracks by each such artist.

for artist in artists_collection.find({"$where": "this.tracks.length > 1"}, {"artist_id":1, "name":1,"num":"$tracks"}):
  artist["num"] = len(artist.get("num"))
  print(artist)
