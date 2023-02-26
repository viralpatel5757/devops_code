import colorgram # cologram lets you extract the color out of any image and put that color in rgb formate.
import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.speed(10)
turtle.colormode(255)
tim.penup()
tim.hideturtle()

colors = colorgram.extract('image.jpg', 30)
color_list = []

for color in colors: # creating tuple of rgb value from colorgram
    rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    color_list.append(rgb_tuple)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()

