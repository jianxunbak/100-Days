from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def back(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def win(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

