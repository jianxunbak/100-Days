from turtle import Screen
from snake import Snake
import time

snake = Snake()

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)  # stop all animations
screen.listen()
screen.onkey(snake.up, "w")
# screen.onkey(snake.down, "s")
# screen.onkey(snake.left, "a")
# screen.onkey(snake.right, "d")


game_on = True

while game_on:
    snake.move()  # run snake class move def
    screen.update()  # update the screen to reflect all changes
    time.sleep(0.1)  # slow down the change


screen.exitonclick()
