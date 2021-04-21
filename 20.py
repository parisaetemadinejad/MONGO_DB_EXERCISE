import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
db = my_client.get_database("restaurant_database2")
my_col = db.get_collection('restaurant')
with open('json_file.json') as f:
    file_data = json.load(f)
i = 0
for _ in db.restaurant.find({
    "$or": [
        {"grades.score": {
            "$lt": 10}},
        {"grades.score": {
            "$eq": 10}}
    ]

}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 0}):
    print(_)
    i += 1
print(i)
