import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
db = my_client.get_database("restaurant_database2")
my_col = db.get_collection('restaurant')
with open('json_file.json') as f:
    file_data = json.load(f)
i = 0
sort_stage = {
    "$sort": {
        "name": pymongo.ASCENDING
    }
}
pipelines = [sort_stage]
docs = my_col.aggregate(pipelines)
for _ in docs:
    print(_)
