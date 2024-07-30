from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor, screen_size):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 5)
        self.color("white")
        self.goto(xcor, ycor)
        self.size = screen_size.window_width()

    def move_left(self):
        new_x = self.xcor() - 20
        if new_x > -(self.size // 2) + 70:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        if new_x < (self.size // 2) - 70:
            self.goto(new_x, self.ycor())
