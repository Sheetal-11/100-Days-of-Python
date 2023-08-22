# The Number Guessing Game

from random import randint

#Welcome
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Guess a number
num = randint(1, 100)
print(f"Pssst, the correct answer is {num}")



