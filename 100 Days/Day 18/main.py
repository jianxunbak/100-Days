# import colorgram
import random
from turtle import Turtle, Screen, colormode

rgb_colours = [
    (252, 244, 248), (219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152),
    (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62),
    (131, 83, 102), (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115),
    (237, 161, 174), (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76),
    (34, 87, 53), (232, 209, 16), (74, 79, 40)
]

colormode(255)
dots = Turtle()
dots.speed("fastest")
dots.shape("circle")

# def change_colour():
#     colour = random.choice(rgb_colours)
#     r = colour[0]
#     g = colour[1]
#     b = colour[2]
#     random_colour = (r, g, b)

start= [-250, -250]
dots.penup()
dots.hideturtle()
dots.setposition(start[0], start[1])


def painting():
    for _ in range(10):
        # change_colour()
        dots.dot(20, random.choice(rgb_colours))
        dots.forward(50)

for _ in range(10):
    painting()
    start[1] += 50
    dots.teleport(dots.setposition(start[0], start[1]))

screen = Screen()
screen.exitonclick()

# colours = colorgram.extract("e2bdacc92bf68d481144397a7c8beef6.jpg", 30)
#
# for item in colours:
#     r = item.rgb[0]
#     g = item.rgb[1]
#     b = item.rgb[2]
#
#     colour_code = (r,g,b)
#     rgb_colours.append(colour_code)
