import json

import pymongo

my_client = pymongo.MongoClient(host="localhost", port=27017)
my_db = my_client["restaurant_database"]
my_col = my_db["restaurant"]
with open('json_file.json') as f:
    file_data = json.load(f)
# my_col.insert_many(file_data)
# 8
score_stage = {
    '$match': {
        'grades.score': {
            "$gt": 90
        }
    }
}
pipelines = [score_stage]
my_docs = my_col.aggregate(pipelines)
i=0
for x in my_docs:
    print(x)
    i+=1
print(i)
