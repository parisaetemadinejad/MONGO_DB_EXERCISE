import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
my_db = my_client["restaurant_database"]
my_col = my_db["restaurant"]
with open('json_file.json') as f:
    file_data = json.load(f)
# 4
for item in my_col.find({},{"restaurant_id": 1, 'name': 1, "borough": 1, 'cuisine': 1,'_id': 0}):
    print(item)
