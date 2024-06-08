#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# use random.choice to randomly pic a letter from the list
password_list = []
for L in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for S in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for N in range(1, nr_symbols + 1):
    password_list += random.choice(numbers)

# randomise password wuth shuffle function. Note that shuffle function can only shuffle list.
PW = list(password_list)
random.shuffle(PW)
new_password = ''.join(PW)

# create a "for" "in" to convert list to string
new_password = ""
for X in PW:
    new_password += X

print(new_password)
