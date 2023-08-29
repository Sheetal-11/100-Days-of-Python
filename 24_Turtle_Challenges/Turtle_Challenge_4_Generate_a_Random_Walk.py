# Challenge 4: Draw a Random Walk
from turtle import Turtle, Screen
from random import choice

t = Turtle()
t.hideturtle()
t.width(8)
t.speed(10)
colors = ["black", "cornflower blue", "navy", "dodger blue", "cyan", "spring green", "dark green", "chartreuse",
          "yellow", "saddle brown", "firebrick", "brown", "dark red", "tomato", "red", "crimson", "light coral",
          "deep pink", "medium violet red", "purple", "magenta", "dark violet", "indigo", "dark slate blue"]
angles = [0, 90, 180, 270]

for _ in range(300):
    t.color(choice(colors))
    # Set the orientation of the turtle to to_angle
    t.setheading(choice(angles))
    t.forward(30)

screen = Screen()
screen.exitonclick()
