from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)   # set screen size
# Bring up a pop-up
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

all_turtles = []   # list where we will store all turtle objects
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
gap = 0

for new_color in colors:
    # for each color create a new turtle
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(new_color)
    all_turtles.append(new_turtle)
    new_turtle.up()  # to stop the turtle from drawing when going from origin to new location
    new_turtle.goto(x=-230, y=-125+gap)
    gap += 40   # vertical gap between each turtle

screen.exitonclick()
