import random

family = ["Mother", "Father", "Aunt", "Uncle", "Brother", "Sister" ]
pairs = {}

for p in range(len(family) // 2):
    pairs[p+1] = ( family.pop(random.randrange(len(family))),
        family.pop(random.randrange(len(family))) )

print(pairs)