from turtle import Turtle

FONT = ("Courier", 24, "bold")
LOCATION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(LOCATION)
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)
