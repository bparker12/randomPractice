import random

giver = [
    {"name": "casie", "pairing": "a"},
    {"name": "kyle", "pairing": "a"},
    {"name": "ben", "pairing": "b"},
    {"name": "meredith", "pairing": "b"},
    {"name": "tyler", "pairing": "c"},
    {"name": "alyssa", "pairing": "c"}]

receiver = [name for name in giver]

def pop_random(lst):
        idx = random.randrange(0, len(lst))
        print(idx)
        print(lst.pop(idx)['name'])

pop_random(giver)