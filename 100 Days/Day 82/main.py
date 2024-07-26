from morse import code

sentence = input(
    "Please provide your sentence to be converted into morse code:\n")
sentence_list = list(sentence)

coded = []
for letters in sentence_list:
  if letters in code:
    letters = code[letters]
    coded.append(letters)

coded_message = "".join(coded)
print(coded_message)
