import time
from turtle import Screen, screensize
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up , key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()           

    # detect if turtle reches the upper Y-axis
    if player.ycor() > 280:
        player.refresh()
        car_manager.level_up()
        scoreboard.increase_score()

    # detect if  the turtle collides with car
    for car in car_manager.all_cars :
        if car.distance(player) < 20:
            scoreboard.game_over() 
            game_is_on = False   
      








screen.exitonclick()
