from art import logo
import random
from replit import clear

print(logo)
print("Welcome to the number guessing game!")


def number():
    def guess_compare():
        if player_guess == answer:
            return f"you got it! the answer is {answer}"
        elif player_guess < answer:
            return "too low"
        elif player_guess > answer:
            return "too high"
        else:
            return "you lose"

    print("I am thinking of a number between 1 and 100.")
    answer = int(random.randint(1, 100))

    print(f"Pssst, the correct answer is {answer}.")

    def attempts():
        difficulty = input(
            "choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5

    attempts = attempts()
    game_over = False

    while not game_over:
        print(f"you have {attempts} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        guess_compare()
        print(guess_compare())
        attempts -= 1
        if attempts == 0:
            game_over = True
            print("you have run out of guesses. You lose")
        if guess_compare() == "you win" or guess_compare() == "you lose":
            game_over = True
            guess_compare()


while input("do you want to play the number game? Type 'yes' or 'no': ").lower() == "yes":
    clear()
    number()
