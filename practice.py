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
    for name in list1:
        print("giver", name['name'])
        findPairing = name['pairing']
        pairingMatch = [x for x in list2 if x['pairing'] == findPairing]
        for name in pairingMatch:
            list2.remove(name)
        chosenPerson = pop_random(list2)
        print("chosenPerson", chosenPerson['name'])
        #send email with "name" as the recepient of email and the chosenPerson as the message body
        for name in pairingMatch:
            list2.append(name)


randomize_pairs(giver, receiver)

