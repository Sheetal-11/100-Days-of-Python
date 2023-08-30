from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)   # set screen size
# Bring up a pop-up
names_string = screen.textinput(title="Enter names", prompt="Enter all the names in one line separated by space")
names = names_string.split(" ")

bets = {}

for name in names:
    bets[name] = screen.textinput(title="Make your bet", prompt=f"Enter {name}'s bet: ")

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

is_race_on = False

if names_string:
    is_race_on = True

while is_race_on:
    # Race starts
    for turtle in all_turtles:
        # End the race if one of the turtles reaches the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            # Declare whether the user won the bet
            winning_color = turtle.pencolor()
            if winning_color in bets.values():
                for name in bets:
                    if bets[name] == winning_color:
                        print(f"{name} won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've all lost! The {winning_color} turtle is the winner!")

        # turtle.speed("slow")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
