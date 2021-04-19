import random

street = ["Aghdasieh", 'Azadi Avenue', 'Damavand Street', 'Doulat', 'Enqelab Street', 'Farmanieh', 'Ferdowsi Street',
          'Imam Hossein Square', 'Jomhuri', 'Kargar Street', 'Keshavarz Boulevard',
          'Khayyam Street', 'Laleh-Zar Street', 'Mirdamad Boulevard', 'Nelson Mandela Boulevard',
          '(Jordan Street) Tehran', 'Nimr Baqir al-Nimr Street', 'Pasdaran (district)', 'Pasteur Street',
          'Rah Ahan Square', 'Seoul Street', 'Shush Street', 'Sohrevardi Street', 'Surena Street', 'Tohid Tunnel',
          'Valiasr Street', ]
borough = ['Nicole Nelson', 'Michael Baker', 'Betty Turner', 'Kevin White', 'Maria Murphy', 'Billy Scott',
           'Willie Allen',
           'Martha Mitchell',
           'Jacqueline Jones', 'Joyce Martinez', 'Lillian Roberts', 'Julia Jenkins', 'Brian Anderson', 'Karen Evans',
           'Angela Rivera', 'Sharon Sanchez', 'Louis Griffin', 'Mark Taylor',
           'Marie Hughes', 'Pamela Thomas', 'Richard James', 'Ruth Watson', 'Phyllis Cooper', 'Benjamin Butler',
           'Sarah Morgan'

           ]
grade = ['A', 'B', 'C', 'D']


# this code select random from list
# print(random.choice(street))
# create random zipcode and handle unique
def zip_code(low_num, high_num, number_num):
    set_sample = set()
    while len(set_sample) < number_num:
        set_sample.add(random.randint(low_num, high_num))
    return set_sample


def score(low_num, high_num):
    return random.randint(low_num, high_num)


def random_from_list(list_input):
    return random.choice(list_input)


# print(zip_code(1000, 3000, 1000))
print(random_from_list(grade))
print(score(0, 100))
