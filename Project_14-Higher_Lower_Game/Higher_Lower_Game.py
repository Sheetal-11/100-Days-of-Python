# Higher Lower Game

from game_data import data
from art import logo, vs
from random import randint

# 4 keys: 'name', 'follower_count', 'description', 'country'

data_copy = data

def pick_entry():
    '''
    returns a random entry from data
    '''
    position = randint(0, len(data) -1)
    # to prevent an entry from repeating itself in a round
    data_copy.pop(position)
    return data_copy[position]

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

print(f"\nA follower count: {A['follower_count']}")
print(f"B follower count: {B['follower_count']}")

choice = user_choice(A, B)
print(choice)

# Find the correct answer
if A['follower_count'] > B['follower_count']:
    answer = A
else:
    answer = B

# Check if user's guess is right or wrong
if answer['follower_count'] == choice['follower_count']:
    print("You're right")
else:
    print("You're wrong.")




