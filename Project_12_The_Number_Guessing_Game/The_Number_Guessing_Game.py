# The Number Guessing Game

from random import randint

#Welcome
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Guess a number
num = randint(1, 100)
print(f"Pssst, the correct answer is {num}")

#Set number of lives
print("\nChoose your difficulty level")
lives = 0

while lives == 0:
    difficulty_level = input("'easy' or 'hard': ")
    
    if difficulty_level == "easy":
        lives = 10
    elif difficulty_level == "hard":
        lives = 5
    else:
        print("Please type a valid answer")

print(f"lives = {lives}")

