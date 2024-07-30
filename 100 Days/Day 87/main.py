from turtle import Screen
from paddle import Paddle
from blocks import Blocks
from random import randint
from ball import Ball
from score import Score
import time

screen_width = 1000
screen_height = 600
paddle_start_x = 0
paddle_start_y = -(screen_height / 2) + 50
ball_start_x = 0
ball_start_y = -(screen_height / 2) + 65
score_loc_y = (screen_height / 2) - 60
win_lose_y = (screen_height / 2) - 100
usable_width = screen_width // 2 - 55
usable_height = screen_height // 2 - 100

screen = Screen()
screen.setup(screen_width, screen_height)
screen.colormode(255)
screen.bgcolor("black")
screen.title("game")
screen.tracer(0)

ball = Ball(xcor=ball_start_x, ycor=ball_start_y)
paddle = Paddle(xcor=paddle_start_x, ycor=paddle_start_y, screen_size=screen)
all_target = Blocks.create_blocks(usable_height=usable_height, usable_width=usable_width)
score = Score(xcor=0, ycor=score_loc_y, targets=len(all_target))


screen.listen()
screen.onkey(fun=paddle.move_left, key="a")
screen.onkey(fun=paddle.move_right, key="d")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() < -usable_width or ball.ycor() > usable_width or ball.ycor() > usable_width:
        ball.bounce_y()

    if ball.xcor() < -usable_width or ball.xcor() > usable_width:
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() < ball_start_y:
        ball.bounce_y()

    if ball.ycor() < paddle_start_y:
        score.lose(win_lose_y)
        game = False

    for target in all_target:
        if ball.distance(target) < 30:
            ball.bounce_y()
            all_target.remove(target)
            target.hideturtle()
            ball.move_speed *= 0.9
            score.add_score()

    if all_target is None:
        score.win(win_lose_y)
        game = False

screen.exitonclick()
