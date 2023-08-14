# -*- coding: utf-8 -*-
#Exercise: Write a program that works out whether 
#if a given number is an odd or even number.

num = int( input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
    
else:
    print(f"{num} is an odd number.")
    
