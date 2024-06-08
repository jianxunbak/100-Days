from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("arial", 40, "italic")
WORD_FONT = ("arial", 60, "bold")

# -----WORDS----- #
try:
    words_to_learn = pandas.read_csv("./data/words to learn.csv")

except FileNotFoundError:
    original_words = pandas.read_csv("./data/french_words.csv")
    words = original_words.to_dict("records")

else:
    words = words_to_learn.to_dict("records")

def random_french_word():
    global flip_card, random_word
    window.after_cancel(flip_card)
    random_word = choice(words)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_card = window.after(3000, english_translation)


def english_translation():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_word["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)


def words_known():
    words.remove(random_word)
    data = pandas.DataFrame(words)
    data.to_csv("./data/words to learn", index=False)
    random_french_word()

# -----UI----- #
# WINDOWS
window = Tk()
window.title("My Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_card = window.after(3000, func=english_translation)

# IMAGE
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# CANVAS CARD
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 265, image="")
canvas.grid(row=0, column=0, columnspan=2)

# CANVAS TEXT
title_text = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word_text = canvas.create_text(400, 265, text="", font=WORD_FONT)

# BUTTON
right_button = Button(image=right_image, border=0, highlightthickness=0, command=words_known)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_image, border=0, highlightthickness=0, command=random_french_word)
wrong_button.grid(row=1, column=1)

random_french_word()

window.mainloop()
