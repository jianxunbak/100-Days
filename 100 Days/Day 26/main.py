student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # print(row)
#     print(row.score)

#     pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(new_dict.keys())

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("what is the name?: ").upper()

new_list = [new_dict[letter] for letter in user_input]
print(new_list)

