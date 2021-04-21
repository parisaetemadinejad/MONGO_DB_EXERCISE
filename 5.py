import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
my_db = my_client["restaurant_database"]
my_col = my_db["restaurant"]
with open('json_file.json') as f:
    file_data = json.load(f)
# 5
query_borough_Richard_James = {"borough": "Marie Hughes"}
my_docs = my_col.find(query_borough_Richard_James)
for x in my_docs:
    print(x)
