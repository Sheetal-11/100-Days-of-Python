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
    position = randint(0, len(data_copy)-1)
    entry = data_copy[position]
    # to prevent an entry from repeating itself in a round
    data_copy.remove(entry)
    return entry

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


end_of_game = False
score = 0

while (not end_of_game) and (score != 49):
        
    A = pick_entry()
    B = pick_entry()
    
    print(f"\nCompare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    
    print(f"\nA follower count: {A['follower_count']}")
    print(f"B follower count: {B['follower_count']}")
    
    choice = user_choice(A, B)
    
    # Find the correct answer
    if A['follower_count'] > B['follower_count']:
        answer = A
    else:
        answer = B
    
    # Check if user's guess is right or wrong
    if answer['follower_count'] == choice['follower_count']:
        score += 1
        print(f"\nYou're right. Current score = {score}")
    else:
        print("You're wrong.")
        print(f"\nSorry, that's wrong. Final score = {score}")
        end_of_game = True

if score == 49:
    print("\nCongratualtions, you've won the game with a full score!")



