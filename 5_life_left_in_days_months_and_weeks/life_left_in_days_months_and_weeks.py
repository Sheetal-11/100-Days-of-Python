#Exercise: Create a program using maths and f-Strings that 
#tells us how many days, weeks, months we have left 
#if we live until 90 years old.

age = int( input("What is your age?: "))

years_left = 90 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")