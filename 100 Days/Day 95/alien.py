from turtle import Turtle


class Alien(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('alien_small_1.gif')
        self.shapesize(stretch_wid=0.3, stretch_len=0.3, outline=0)
        self.penup()
        self.goto(x=x, y=y)
