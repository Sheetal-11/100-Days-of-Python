# The Number Guessing Game

from random import randint
from art_number_guessing_game import logo

#Welcome
print(logo)
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Guess a number
num = randint(1, 100)

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

while lives > 0:
    print(f"You have {lives} attempts remaining.")
    guess = int( input("\nGuess a number: "))
    
    if guess < num:
        print("Too low")
        print("Guess again")
    elif guess > num:
        print("Too high")
        print("Guess again")
    else:
        print(f"You got it! The answer was {num}.")
        break
    
    lives -= 1
    
if lives == 0:
    print("You run out of guesses. You lose.")
    print(f"The number was {num}.")

