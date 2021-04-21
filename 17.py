import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
db = my_client.get_database("restaurant_database2")
my_col = db.get_collection('restaurant')
with open('json_file.json') as f:
    file_data = json.load(f)
i = 0
# for _ in db.restaurant.find({
#     "$and": [
#         {
#             "$or": [
#                 {"cuisine": "cuisine6"},
#                 {"cuisine": "cuisine1"}
#             ]
#         },
#         {
#             "borough": "Marie Hughes"
#         }
#     ]
# }):
for _ in db.restaurant.find({
    "$or": [
        {"cuisine": "cuisine1"},
        {"cuisine": "cuisine6"}
    ],
    "borough": "Marie Hughes"
}):
    print(_)
    i += 1
print(i)
