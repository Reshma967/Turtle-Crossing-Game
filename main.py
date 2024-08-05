import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
carmanager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create()
    carmanager.move()
    scoreboard.leve()

    for car in carmanager.cars:
        if car.distance(player)<20:
            scoreboard.over()
            game_is_on=False

    if player.ycor()>280:
        player.reset()
        scoreboard.inc()
        carmanager.inc()






screen.exitonclick()