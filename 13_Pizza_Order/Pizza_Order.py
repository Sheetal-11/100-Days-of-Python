# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 17:23:15 2023

@author: sheet
"""

#Exercise: Based on a user's order, work out their final bill.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N:  ")
extra_cheese = input("Do you want extra cheese? Y or N:  ")

bill = 0

if str.lower(size) == "s":
    bill = 15
    if str.lower(add_pepperoni) == "y":
        bill += 2
    
elif str.lower(size) == "m":
    bill = 20
    if str.lower(add_pepperoni) == "y":
        bill += 3

elif str.lower(size) == "l":
    bill = 25
    if str.lower(add_pepperoni) == "y":
        bill += 3
    
else:
    print("\nWrong input. Please try again.")

if str.lower(extra_cheese) == "y":
    bill += 1

print(f"\nYour total bill is ${bill}")

