# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:50:27 2023

@author: sheet
"""

#Exercise: Write a program that interprets 
#the Body Mass Index (BMI) based on a user's weight and height.

weight = float( input("Enter your weight in kg: "))
height = float( input("Enter your height in m: "))

print(f"\nweight = {weight} kg")
print(f"height = {height} m\n")

bmi = round( weight / height ** 2, 1)

if bmi < 16:
    print(f"Your BMI is {bmi}, you are underweight (severe thinness).")

elif bmi < 17:
    print(f"Your BMI is {bmi}, you are underweight (moderate thinness).")
    
elif bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight(mild thinness).")

elif bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight.")

elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight (pre-obese).")

elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese (Class I).")

elif bmi < 40:
    print(f"Your BMI is {bmi}, you are obese (Class II).")

else:
    print(f"Your BMI is {bmi}, you are obese (Class III).")