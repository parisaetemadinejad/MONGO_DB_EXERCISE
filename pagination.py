import json
import pymongo

page = 1
pagination_by = 5

my_client = pymongo.MongoClient(host="localhost", port=27017)
my_db = my_client["restaurant_database2"]
my_col = my_db["restaurant"]
with open('json_file.json') as f:
    file_data = json.load(f)

for i in range(200):
    print("you are in page ", i)
    for _ in my_db.restaurant.find().skip(pagination_by * (i - 0)).limit(pagination_by):
        print(_)
        page += 1
