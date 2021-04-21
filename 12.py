import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
db = my_client.get_database("restaurant_database2")
my_col = db.get_collection('restaurant')
with open('json_file.json') as f:
    file_data = json.load(f)
# my_col.insert_many(file_data)
i = 0
cuisine_stage = {
    '$match': {
        'cuisine': {
            "$ne": "cuisine5"
        },
        'grades.score': {
            "$gt": 70
        },
        'address.coord': {
            "$lt": -65.754168
        }
    }}
pipelines = [cuisine_stage]
my_docs = my_col.aggregate(pipelines)
n = 0
for x in my_docs:
    print(x)
    n += 1
print(n)
