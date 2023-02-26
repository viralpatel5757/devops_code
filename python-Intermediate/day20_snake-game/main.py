# build snake-game (following this 7 steps)
# 1) create snake body
# 2) move snake 
# 3) ceate snake food
# 4) detect collision with food
# 5) create score board
# 6) detect collision with wall
# 7) detect collision with tail.
# we will make snake class, food class and score class

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up") # onkey rewuire two arguments : 1) key and 2) function
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # call move() function from class Snake using object snake
    snake.move() 

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect tail collision.
    # if   head collides with any segment in the tail then trigger game_over:

    # below code works the same except it does not use slicing.
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
 

screen.exitonclick()