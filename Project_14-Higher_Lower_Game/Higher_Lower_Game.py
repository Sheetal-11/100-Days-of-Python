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
    
    
A = pick_entry()
B = pick_entry()

print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")



