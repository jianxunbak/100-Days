from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, x, y, head):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=.2, stretch_len=0.2, outline=0)
        self.setheading(head)
        self.color(255, 255, 255)
        self.penup()
        self.goto(x=x, y=y)
        self.speed('fast')

    def shoot(self):
        self.forward(10)
