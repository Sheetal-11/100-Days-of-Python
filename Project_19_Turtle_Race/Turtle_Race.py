from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)   # set screen size
# Bring up a pop-up
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Make the turtle go to the start of the line (to the left edge)
tim.up()   # to stop turtle from drawing when going from origin to new location
tim.goto(x=-230, y =-100)

screen.exitonclick()
