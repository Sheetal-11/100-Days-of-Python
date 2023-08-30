# Challenge 1: Draw a Square
from turtle import Turtle, Screen

t = Turtle()
t.width(3)
for _ in range(4):
    t.forward(150)
    t.left(90)

screen = Screen()
screen.mainloop()
