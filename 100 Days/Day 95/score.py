from turtle import Turtle


class Score(Turtle):
    def __init__(self, xcor, ycor, alien):
        super().__init__()
        self.total_alien = len(alien)
        self.color('white')
        self.penup()
        self.goto(xcor, ycor)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'{self.score}/{self.total_alien}', align='center', font=('Arial', 20, 'bold'))

    def lose(self, xcor, ycor):
        self.goto(0, 0)
        self.write(arg='YOU LOSE!', align='center', font=('Arial', 100, 'bold'))

    def win(self, xcor, ycor):
        self.goto(xcor, ycor)
        self.write(arg='YOU WIN!', align='center', font=('Arial', 20, 'bold'))

    def add_score(self):
        self.score += 1
        self.update_score()
