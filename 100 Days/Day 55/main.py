from flask import Flask
from random import randint

app = Flask(__name__)

rand_num = randint(0, 9)
print(rand_num)

@app.route("/")
def home():
    return ('<h1 style="text-align: center">Guess a number between 0 and 9</h1>'
            '<img src = "https://i.giphy.com/media/v1'
            '.Y2lkPTc5MGI3NjExMjExcWdnNjNoMDVja2x2YTc0ZjVua3hwaXFscnkzN2poa3N0dnE2bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4JVTF9zR9BicshFAb7/giphy.gif" style="display: block; margin-left: auto; margin-right: auto;">'
            )


@app.route("/<int:guess>")
def num(guess):
    if guess < rand_num:
        return ('<h1 style="text-align: center">Guess Wrong! Too Low!</h1>'
                '<img src = "https://i.giphy.com/media/v1'
                '.Y2lkPTc5MGI3NjExYnYwcHAyN3h4bjBlNHg0a2ZmaGZ3MHUxaTVicXIzemNucDhpZWFyZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XJLEXP9xEJRevqXxnR/giphy.gif" style="display: block; margin-left: auto; margin-right: auto;">'
                )
    elif guess > rand_num:
        return ('<h1 style="text-align: center">Guess Wrong! Too High!</h1>'
                '<img src = "https://i.giphy.com/media/v1'
                '.Y2lkPTc5MGI3NjExMDhicjE3dnJobGdwaTJjaWt6cWNybno1eGlyeHBsbWZhY2J6dmJ5cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Gj61Dk0lT7UwvddTuP/giphy.gif" style="display: block; margin-left: auto; margin-right: auto;">'
                )
    else:
        return ('<h1 style="text-align: center">Guess Correct! YAYS!</h1>'
                f'<p style="text-align: center"> The number was : {rand_num}</p>'
                '<img src = "https://i.giphy.com/media/v1'
                '.Y2lkPTc5MGI3NjExNzloMHcxandpczY3czd1YnRoeTJ3MWF6cHVuZWoxdWp0NjRiNTZ0byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IwAZ6dvvvaTtdI8SD5/giphy.gif" style="display: block; margin-left: auto; margin-right: auto;">'
                )

if __name__ == "__main__":
    app.run(debug=True)
