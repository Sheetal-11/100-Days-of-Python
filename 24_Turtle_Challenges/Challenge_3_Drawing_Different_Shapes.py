# Challenge 3: Drawing Different Shapes
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# Each shape has to be drawn with a random color
# Each side = 100
from turtle import Turtle, Screen
from random import choice

t = Turtle()
t.width(3)
colors = ["black", "cornflower blue", "navy", "dodger blue", "cyan", "spring green", "dark green", "chartreuse",
          "yellow", "saddle brown", "firebrick", "brown", "dark red", "tomato", "red", "crimson", "light coral",
          "deep pink", "medium violet red", "purple", "magenta", "dark violet", "indigo", "dark slate blue"]

for polygon in range(3, 11):
    # polygon tells what polygon it's going to draw in this loop
    angle = 360 / polygon
    t.color(choice(colors))
    for sides in range(polygon):
        # Draw the sides of the polygon
        t.forward(100)
        t.right(angle)

screen = Screen()
screen.exitonclick()
