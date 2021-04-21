import json
import random

import randomtimestamp as randomtimestamp

STREET = ["Aghdasieh", 'Azadi Avenue', 'Damavand Street', 'Doulat', 'Enqelab Street', 'Farmanieh', 'Ferdowsi Street',
          'Imam Hossein Square', 'Jomhuri', 'Kargar Street', 'Keshavarz Boulevard',
          'Khayyam Street', 'Laleh-Zar Street', 'Mirdamad Boulevard', 'Nelson Mandela Boulevard',
          '(Jordan Street) Tehran', 'Nimr Baqir al-Nimr Street', 'Pasdaran (district)', 'Pasteur Street',
          'Rah Ahan Square', 'Seoul Street', 'Shush Street', 'Sohrevardi Street', 'Surena Street', 'Tohid Tunnel',
          'Valiasr Street', ]
BOROUGH = ['Nicole Nelson', 'Michael Baker', 'Betty Turner', 'Kevin White', 'Maria Murphy', 'Billy Scott',
           'Willie Allen',
           'Martha Mitchell',
           'Jacqueline Jones', 'Joyce Martinez', 'Lillian Roberts', 'Julia Jenkins', 'Brian Anderson', 'Karen Evans',
           'Angela Rivera', 'Sharon Sanchez', 'Louis Griffin', 'Mark Taylor',
           'Marie Hughes', 'Pamela Thomas', 'Richard James', 'Ruth Watson', 'Phyllis Cooper', 'Benjamin Butler',
           'Sarah Morgan'

           ]
CUISINE = [
    'cusine1', 'cusine2', 'cusine3', 'cusine4', 'cusine5', 'cusine6', 'cusine7', 'cusine8'
    , 'cusine1', 'cusine2', 'cusine3', 'cusine4', 'cusine5', 'cusine6', 'cusine7', 'cusine8'
    , 'cusine1', 'cusine2', 'cusine3', 'cusine4', 'cusine5', 'cusine6', 'cusine7', 'cusine8'
]
GRADE = ['A', 'B', 'C', 'D']


def zip_code(low_num, high_num, number_num):
    set_sample = set()
    while len(set_sample) < number_num:
        set_sample.add(random.randint(low_num, high_num))
    return set_sample


def score(low_num, high_num):
    return random.randint(low_num, high_num)


def random_from_list(list_input):
    return random.choice(list_input)


def create_coord(start, end):
    return [random.uniform(start, end), random.uniform(start, end)]


json_data = []
for i in range(1000):
    data = {}
    data['address'] = {
                          'building': score(1000, 2000),
                          'coord': create_coord(-100, 100),
                          'street': random.choice(STREET),
                          'zipcode': zip_code(1000, 5000, 5).pop(),
                      },
    data['borough'] = random.choice(BOROUGH)
    data['cuisine'] = random.choice(CUISINE)
    data['grades'] = [
        {
            'date':
                {
                    'date': score(1000000000, 9000000000)
                },
            'grade': random.choice(GRADE),
            'score': score(0, 100)

        },
        {
            'date':
                {
                    'date': score(1000000000, 9000000000)
                },
            'grade': random.choice(GRADE),
            'score': score(0, 100)

        },
        {
            'date':
                {
                    'date': score(1000000000, 9000000000)
                },
            'grade': random.choice(GRADE),
            'score': score(0, 100)

        }
    ]
    data['name'] = random.choice(BOROUGH)
    data['restaurant_id'] = score(10000000, 70000000)
    json_data.append(data)
print(json_data)
with open('json_file.json', 'w') as outfile:
    json.dump(json_data, outfile)
