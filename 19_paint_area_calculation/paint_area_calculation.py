#Exercise: Area Calculation
import math

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area/cover)
    print(f"The surface area to paint is {area}sq.m.")
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall in m: "))
test_w = int(input("Width of wall in m: "))
coverage = 5  #This parameter tells 1 can of paint can cover this much square meters of area
paint_calc(height=test_h, width=test_w, cover=coverage)


