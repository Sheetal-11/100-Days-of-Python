#Exercise: Write a program which will select a random name from a list of names.
#The person selected will have to pay for everybody's food bill.
#You can't use random.choice() here

import random

names_string = input("Give me everybody's names, separated by a comma.\n")

names = names_string.split(", ")

index_pick = random.randrange(len(names))

chosen = names[index_pick]

print(f"{chosen} is going to buy the meal today!")

