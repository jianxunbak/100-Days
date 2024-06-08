from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

race_on = False
turtles = ["tim", "john", "ben", "jane", "david", "mary"]
colour = ["red", "blue", "green", "purple", "cyan", "magenta"]
y_position = [-125, -75, -25, 25, 75, 125]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter {colour}: ")


for turtles_type in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour[turtles_type])
    new_turtle.penup()
    new_turtle.goto(-200, y_position[turtles_type])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"you won! {winner} is the winner!")
            else:
                print(f"you lose! {winner} is the winner!")


screen.exitonclick()
