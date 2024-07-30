from turtle import Turtle
from random import randint


class Blocks(Turtle):
    def __init__(self, xcor, ycor, x, y, color):
        super().__init__()
        self.shape("square")
        self.shapesize(x, y)
        self.penup()
        self.color(color)
        self.goto(xcor, ycor)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

    @staticmethod
    def create_blocks(usable_height, usable_width):
        all_target = []
        for number in range(0, usable_height, 30):
            ycor = number
            for num in range(-usable_width, usable_width, 80):
                y = randint(1, 3)
                color = Blocks.random_color()
                target = Blocks(xcor=num, ycor=ycor, x=1, y=y, color=color)
                all_target.append(target)
        return all_target
