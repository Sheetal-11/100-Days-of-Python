# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:48:30 2023

@author: sheet
"""

#Exercise: You are going to write a program that 
#tests the compatibility between two people.

name1 = input("name1 = ")
name2 = input("name2 = ")

combined = name1 + name2

first_digit = 0
second_digit = 0

first_digit += combined.casefold().count('t')
first_digit += combined.casefold().count('r')
first_digit += combined.casefold().count('u')
first_digit += combined.casefold().count('e')

second_digit += combined.casefold().count('l')
second_digit += combined.casefold().count('o')
second_digit += combined.casefold().count('v')
second_digit += combined.casefold().count('e')

score = int( str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")

elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")


