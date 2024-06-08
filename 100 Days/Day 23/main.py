import time
from turtle import Screen
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
screen.onkey(fun=player.move, key="w")
screen.onkey(fun=player.back, key="s")
screen.onkey(fun=player.left, key="a")
screen.onkey(fun=player.right, key="d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    if player.win():
        scoreboard.level_up()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

