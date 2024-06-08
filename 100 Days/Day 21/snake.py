from turtle import Turtle

STARTING_LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]  # determine starting location of turtles created
DISTANCE = 20

# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0


class Snake:

    def __init__(self):
        self.starting_snake = []  # create a list to store all turtles created to be use in other functions
        self.create_snake()
        self.head = self.starting_snake[0]

    def create_snake(self):
        for items in range(0, 3):  # loop through range of 0, 1, 2 and execute the following in every loop
            segments = Turtle("square")
            segments.color("white")
            segments.penup()
            segments.goto(STARTING_LOCATIONS[items])  # use starting location list to assign location
            self.starting_snake.append(segments)  # append turtles created in every loop into starting snake list

    def move(self):
        start = len(self.starting_snake) - 1
        for items in range(start, 0, -1):  # range function have start, stop, step value
            x_cor = self.starting_snake[items - 1].xcor()
            y_cor = self.starting_snake[items - 1].ycor()
            self.starting_snake[items].goto(x_cor, y_cor)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.setheading() != 270:
            self.head.setheading(90)

    # def left(self):
    #     if self.head.setheading() != RIGHT:
    #         self.head.setheading(LEFT)
    #
    # def right(self):
    #     if self.head.setheading() != LEFT:
    #         self.head.setheading(RIGHT)
    #
    # def down(self):
    #     if self.head.setheading() != UP:
    #         self.head.setheading(DOWN)
