from turtle import Turtle, Screen
import pandas

screen = Screen()
us_map = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
us_map.shape(image)

data = pandas.read_csv("50_states.csv")
states_name = data.state.to_list()

guessed_states = []

while len(guessed_states) < len(states_name):
    player_guess = screen.textinput(title=f"{len(guessed_states)} state guessed correctly",
                                    prompt="what is the state").title()

    if player_guess == "Exit":
        missing_states = [items for items in states_name if items not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn")
        break

    if player_guess in states_name:
        name = Turtle()
        name.penup()
        name.hideturtle()
        correct_state = data[data.state == player_guess]
        name.goto(int(correct_state.x), int(correct_state.y))
        name.write(player_guess)
        guessed_states.append(player_guess)
