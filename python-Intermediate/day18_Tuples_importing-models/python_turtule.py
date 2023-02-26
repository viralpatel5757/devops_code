import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pencolor("red")
###############################################################
# Draw Square.
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

########### Challenge 2 - Draw a Dashed Line ########

# for _ in range(50):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

########### Challenge 3 - Draw Shapes ########
# num_sides = 3
#
#
# def angle():
#     angle_calculated = float(360/num_sides)
#     return angle_calculated
#
#
# while num_sides < 11:
#     angle_used = angle()
#     for _ in range(0, num_sides):
#         tim.forward(100)
#         tim.left(angle_used)
#     num_sides += 1

########### Challenge 4 - Random Walk ########
# import random
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.pensize(10)
# tim.speed("fastest")
#
# for _ in range(0, 500):
#     angle = 90 * random.randint(1, 5)
#     tim.pencolor(random.choice(colours))
#     tim.forward(20)
#     tim.right(angle)


####### Challange 5: Use colormode() to change the color of turtul module ############
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_tuple = (r, g, b)
#     return rgb_tuple
#
#
# tim.pensize(10)
# tim.speed("fastest")
#
# for _ in range(0, 500):
#     angle = 90 * random.randint(1, 5)
#     tim.pencolor(random_color())
#     tim.forward(20)
#     tim.right(angle)

########### Challenge 5 - Spirograph ########
# turtle.colormode(255)
# tim.speed("fastest")


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)


screen = Screen()
screen.exitonclick()