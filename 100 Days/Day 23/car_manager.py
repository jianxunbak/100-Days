import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []   # this will only have 1 car object as it only run create_care 1 time
        self.create_car()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):   # this will only create 1 car object
        dice = random.randint(1,6)
        if dice == 6:
            new_y = random.randint(-240, 240)
            car = Turtle()
            car .penup()
            car .shape("square")
            car .shapesize(1, 2)
            car .color(random.choice(COLORS))
            car .goto(300, new_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

