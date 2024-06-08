search_text = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    all_names = file.readlines()

with open("./Input/letters/starting_letter.txt") as file:
    contents = file.read()

for items in all_names:
    strip = items.strip()
    new_letter = contents.replace(search_text, strip)
    with open(f"./Output/ReadyToSend/letter_for_{strip}.txt", "w") as file:
        file.write(new_letter)