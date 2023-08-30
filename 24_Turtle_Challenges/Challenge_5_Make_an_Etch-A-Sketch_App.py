Makfrom turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def counter_clockwise():
    pass


def clockwise():
    pass


def clear_drawing():
    pass


screen.listen()
screen.onkeypress(key="w", fun=forwards)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="c", fun=clear_drawing)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.exitonclick()
