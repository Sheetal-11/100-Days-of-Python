# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:10:36 2023

@author: sheet
"""

#Exercise: Write a program that 
#adds the digits in a 2 digit number. 
#e.g. if the input was 35, then the output should be 3 + 5 = 8

num = input('Enter a two digit number: ')

first_digit = int(num[0])
second_digit = int(num[1])

result = first_digit + second_digit

print(result)

