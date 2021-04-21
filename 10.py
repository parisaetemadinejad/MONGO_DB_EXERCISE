import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
my_db = my_client["restaurant_database"]
my_col = my_db["restaurant"]
with open('json_file.json') as f:
    file_data = json.load(f)
# 10
latitude_stage = {

    "$match": {'address.coord': {
        '$lt': -95.754168
    }

    }
}

pipelines = [latitude_stage]
my_docs = my_col.aggregate(pipelines)
for x in my_docs:
    print(x)
