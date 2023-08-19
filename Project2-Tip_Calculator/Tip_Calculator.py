# -*- coding: utf-8 -*-
#Welcome
print('Welcome to the tip calculator!')

total_bill = float( input('What was the total bill? $'))
tip_percent = int( input('What percentage tip would you like to give? 10, 12 or 15?: '))
people = int( input('How many people to split the bill? '))

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

each_person = total_bill * (1 + (0.01 * tip_percent)) / people
each_person = "{:.2f}".format(each_person)

print(f'Each person should pay: ${each_person}')


