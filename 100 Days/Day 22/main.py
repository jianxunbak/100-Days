from turtle import Screen
from ball import Ball
from line import Line
from score import Score
from paddle import Paddle
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Ping Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
score = Score()
line = Line()

screen.listen()
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    line.draw_line()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed * 0.9

    if ball.xcor() > 380:
        score.l_point()
        ball.move_speed = 0.1
        ball.reset()

    if ball.xcor() < -380:
        score.r_point()
        ball.move_speed = 0.1
        ball.reset()



screen.exitonclick()
