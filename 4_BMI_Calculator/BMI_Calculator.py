# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:47:34 2023

@author: sheet
"""

#Exercise: Write a program that 
#calculates the Body Mass Index (BMI) from a user's weight and height.
# BMI = weight(kg) / height(m) ** 2

weight = float( input('Enter weight in kg: '))
height = float( input('Enter height in m: '))

print(f'\nweight = {weight} kg')
print(f'height = {height} m')

bmi = weight / height ** 2
print('\nBMI = ', round(bmi))

