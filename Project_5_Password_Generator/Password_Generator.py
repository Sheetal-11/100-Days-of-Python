# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int( input("How many letters would you like in your password?\n"))
nr_symbols = int( input("How many symbols would you like?\n"))
nr_numbers = int( input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

ez_password = ''

for letter in range(nr_letters):
    pick = random.choice(letters)
    ez_password += pick

for symbol in range(nr_symbols):
    pick = random.choice(symbols)
    ez_password += pick
    
for number in range(nr_numbers):
    pick = random.choice(numbers)
    ez_password += pick    

# print(f"Your easy password could be: {ez_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ''

shuffle = random.sample(ez_password, k=len(ez_password))
#it returns a list, so we combine all elements and make a string

for element in shuffle:
    password += element

print(f"Your password is: {password}")

