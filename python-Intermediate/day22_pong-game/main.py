# 1) create  the screen
# 2) create and move the paddle
# 3) create another paddle
# 4) create the ball and make it move
# 5) detect collision with wall and bounce
# 6) detect collision with paddle
# 7) detect when paddle misses
# 8) kepp the score.

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My PONG game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up") # onkey rewuire two arguments : 1) key and 2) function
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w") 
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # detect the collsion with upper or lower wall
        if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()

        # detect the collsion with right or left paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
                ball.bounce_x()
          
        # detect when right paddle misses the ball        
        if ball.xcor() > 380:
                ball.refresh()
                ball.bounce_x()
                scoreboard.l_point()
                scoreboard.update_scoreboard()
        
        # detect when left paddle misses the ball
        if ball.xcor() < -380:
                ball.refresh() 
                ball.bounce_x()  
                scoreboard.r_point()   
                scoreboard.update_scoreboard()  

               










screen.exitonclick()