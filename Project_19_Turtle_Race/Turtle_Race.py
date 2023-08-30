from turtle import Turtle, Screen
from random import randint

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

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    # Race starts
    for turtle in all_turtles:
        # End the race if one of the turtles reaches the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            # Declare whether the user won the bet
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # turtle.speed("slow")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
