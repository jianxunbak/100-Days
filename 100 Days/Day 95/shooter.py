from turtle import Turtle


class Shooter(Turtle):
    def __init__(self, x, y, screen_width):
        super().__init__()
        self.shape('triangle')
        self.shapesize(stretch_wid=0.6, stretch_len=0.3, outline=0)
        self.color(24, 255, 0)
        self.penup()
        self.setheading(90)
        self.goto(x=x, y=y)
        self.width = screen_width / 2

    def move_left(self):
        new_x = self.xcor() - 10
        if new_x < self.xcor() and self.xcor() > -(self.width - 20):
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 10
        if new_x > self.xcor() and self.xcor() < (self.width - 20):
            self.goto(new_x, self.ycor())

