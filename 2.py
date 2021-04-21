import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
my_db = my_client["restaurant_database"]
my_col = my_db["restaurant"]
with open('json_file.json') as f:
    file_data = json.load(f)
# 2
samples = my_col.find()
for _ in samples:
    print(_)
