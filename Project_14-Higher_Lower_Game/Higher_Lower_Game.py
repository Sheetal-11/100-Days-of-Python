# Higher Lower Game

from game_data import data
from art import logo, vs
from random import randint

# 4 keys: 'name', 'follower_count', 'description', 'country'

def pick_entry():
    '''
    returns a random entry from data
    '''
    position = randint(0, len(data) -1)
    return data[position]
    

print(pick_entry())



