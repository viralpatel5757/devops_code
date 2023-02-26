# listen() method
# goal : move turtle forward when user presses "space" on keyboard.
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)



screen.listen()
screen.onkey(key="space", fun=move_forward) # here we are passing function as 'fun' , you will notice that we do not use parenthesis here.
screen.exitonclick()

