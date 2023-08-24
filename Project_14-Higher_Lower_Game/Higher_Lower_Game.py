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

def user_choice(var_a, var_b):
    '''
    Takes 2 dictionary entries and returns the one that the user selects

    '''
    print("\nWho has more followers?")
    user_input = input("'A' or 'B': ").lower()
    if user_input == 'a':
        choice = var_a
    elif user_input == 'b':
        choice = var_b
    else:
        print("Please type a valid option")
        choice = user_choice(var_a, var_b)
    return choice

    
A = pick_entry()
B = pick_entry()

print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

choice = user_choice(A, B)
print(choice)



