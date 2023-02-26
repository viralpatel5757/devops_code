# challange: mover turtle by pressing 'w'=forward, 's'= backwords, 'a'= counter-clockwise, 'd' = clockwise. 

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_clockwise():
    tim.right(5)

def turn_counter_clockwise():
    tim.left(5)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()    


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
