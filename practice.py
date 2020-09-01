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
        return lst.pop(idx)


def randomize_pairs(list1, list2):
    pairs = {}
    for counter, name in enumerate(list1):
        findPairing = name['pairing']
        pairingMatch = [x for x in list2 if x['pairing'] == findPairing]
        for person in pairingMatch:
            list2.remove(person)
        chosenPerson = pop_random(list2)
        for person in pairingMatch:
            list2.append(person)
        pairs[counter+1] = (name['name'], chosenPerson['name'])
        # print("giver", name['name'])
        # print("chosenPerson", chosenPerson['name'])
        print(pairs)

working = False
while not working:
    try:
        randomize_pairs(giver, receiver)
        working = True
    except ...:
        pass


