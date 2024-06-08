from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_player = 0
        self.r_player = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_player, align="center", font=("Arial", 70, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_player, align="center", font=("Arial", 70, "normal"))

    def l_point(self):
        self.l_player += 1
        self.update_score()

    def r_point(self):
        self.r_player += 1
        self.update_score()
