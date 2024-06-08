from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.goto(xcor, ycor)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
