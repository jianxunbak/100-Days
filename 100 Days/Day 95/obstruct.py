from turtle import Turtle


class Obstruct(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=0.3, stretch_len=0.15, outline=0)
        self.penup()
        self.goto(x=x, y=y)
