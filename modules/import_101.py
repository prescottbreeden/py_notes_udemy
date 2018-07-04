import random

x = random.choice(["apple", "banana", "cherry", "durian"])
y = random.randint(1, 100)
print(x, y)

# Aliasing:

import random as r

x = r.choice(["apple", "banana", "cherry", "durian"])
y = r.randint(1, 100)
print(x, y)

# Importing methods directly:

from random import choice, randint

x = choice(["apple", "banana", "cherry", "durian"])
y = randint(1, 100)
print(x, y)

# Importing methods directly with aliasing:

from random import choice as pick, randint as magic_number_chooser

x = pick(["apple", "banana", "cherry", "durian"])
y = magic_number_chooser(1, 100)
print(x, y)

# ----------------------------------

# Exercise:
# ---------

import keyword

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False
