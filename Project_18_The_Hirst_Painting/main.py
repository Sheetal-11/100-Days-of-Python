# import colorgram
#
# rgb_colors = []
# # Extract top 30 colors from image.jpg
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# -------------------------------------

from turtle import Turtle, Screen
import turtle
import random

t = Turtle()
t.speed("fastest")
t.hideturtle()
turtle.colormode(255)
t.up()  # Turtle can put dots with pen up

color_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
    (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (12, 70, 64), (107, 127, 153),  (176, 192, 208), (168, 99, 102)
]

dimension = 20   # number x number dot matrix
gap = 30   # gap between dots and lines

start_x = - (dimension * gap) / 2
start_y = - (dimension * gap) / 2

y = 0
for line_number in range(dimension):    # Number of lines
    # Change line number:
    t.goto(start_x, start_y+y)
    for _ in range(dimension):    # Number of dots in a line
        # Create one line of 10 dots
        color = random.choice(color_list)
        t.dot(10, color)
        t.forward(gap)
    y += gap

screen = Screen()
screen.exitonclick()
