from turtle import Turtle


class Score(Turtle):
    def __init__(self, xcor, ycor, targets):
        super().__init__()
        self.total_target = targets
        self.color('white')
        self.penup()
        self.goto(xcor, ycor)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'{self.score}/{self.total_target}', align='center', font=('Arial', 50, 'bold'))

    def lose(self, ycor):
        self.goto(0, ycor)
        self.write(arg='YOU LOSE!', align='center', font=('Arial', 30, 'bold'))

    def win(self, ycor):
        self.goto(0, ycor)
        self.write(arg='YOU WIN!', align='center', font=('Arial', 30, 'bold'))

    def add_score(self):
        self.score += 1
        self.update_score()
