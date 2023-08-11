# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:10:50 2023

@author: sheet
"""

# Exercise: Write a program that 
# switches the values stored in the variables a and b.

a = input('\na = ')
b = input ('b = ')

c = a
a = b
b = c

print('\na = ' + a)
print('b = ', b)