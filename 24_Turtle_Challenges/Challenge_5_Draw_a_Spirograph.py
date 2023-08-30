# Challenge 5: Draw a Spirograph
import turtle
from turtle import Turtle, Screen
from random import randint

t = Turtle()
t.speed(0)
# Return the colormode or set it to 1.0 or 255.
# Subsequently, r, g, b values of color triples have to be in the range 0…*cmode*.
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    """
    This function draws spirograph where the gap between each circle is size_of_gap
    :param size_of_gap: int
    :return: None
    """
    for _ in range(int(360/size_of_gap)):
        t.pencolor(random_color())
        t.circle(100)
        current_heading = t.heading()  # Returns the current heading
        t.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
