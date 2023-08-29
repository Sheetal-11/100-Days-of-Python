# Challenge 2: Draw a Dashed Line
from turtle import Turtle, Screen

t = Turtle()
t.width(3)
t.color("red", "DarkGreen")
# Draw a square
for _ in range(4):
    # Draw a Dashed lime:
    for _ in range(10):
        t.forward(10)
        t.up()
        t.forward(10)
        t.down()
    t.left(90)

screen = Screen()
screen.exitonclick()
