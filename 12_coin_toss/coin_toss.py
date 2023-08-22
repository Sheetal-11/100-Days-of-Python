#Exercise: Write a virtual coin toss program.

import random

# one way:
# coin = ['Head', 'Tails']
# random.choice(coin)

toss = random.randint(0, 1)

if toss == 0:
    print("Heads")

else:
    print("Tails")

