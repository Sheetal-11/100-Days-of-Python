# Generate Random RGB color
import turtle
from turtle import Turtle, Screen
from random import choice, randint

t = Turtle()
t.hideturtle()
t.width(8)
t.speed(10)
# Return the colormode or set it to 1.0 or 255.
# Subsequently r, g, b values of color triples have to be in the range 0..*cmode*.
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


angles = [0, 90, 180, 270]

for _ in range(300):
    t.pencolor(random_color())
    # Set the orientation of the turtle to to_angle
    t.setheading(choice(angles))
    t.forward(30)

screen = Screen()
screen.exitonclick()
