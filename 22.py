import json
import time
import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
db = my_client.get_database("restaurant_database2")
my_col = db.get_collection('restaurant')
with open('json_file.json') as f:
    file_data = json.load(f)
my_col.insert_many(file_data)
i = 0
for _ in db.restaurant.find({
    "grades.date": time.mktime(time.strptime('2014-08-11 00:00:00', '%Y-%m-%d %H:%M:%S')),
    "grades.grade": "A",
    "grades.score": 11
},
        {"restaurant_id": 1, "name": 1, "grades": 1}):
    print(_)
    i += 1
print(i)
print(time.mktime(time.strptime('2014-08-11 00:00:00', '%Y-%m-%d %H:%M:%S')))