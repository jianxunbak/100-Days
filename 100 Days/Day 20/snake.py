from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """creates the snake and places it in the base location"""
        # __init__ is to run whatever that is below everytime the class object is created.
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # this line is to use a range to loop through the segments. get hold of the last item 1st (using the len
            # function to determine how many items r there in the list), then progress down to the 1st item. the last
            # digit is the step "-1" to run the loop backwards.

            new_x = self.segments[seg_num - 1].xcor()
            # this line is to get hold of the x position of the segment in front of the current segment

            new_y = self.segments[seg_num - 1].ycor()
            # this line does the same thing as the line above but for y location.

            self.segments[seg_num].goto(new_x, new_y)
            # this line uses the x and y location determine in 2 codes above and assign it to the current segment.
            # By doing this, the current segment will always be trying to be following the segment in front
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
