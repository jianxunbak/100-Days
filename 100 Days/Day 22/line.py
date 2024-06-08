from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.teleport(0, 500)
        self.setheading(270)
        self.width(3)

    def draw_line(self):
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
