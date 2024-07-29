import tkinter as tk
import time
import random
from words import word

start_time = 0
end_time = 0
key_count = 0
typing_speed = 0


def generate_sentence():
    words = random.sample(word, 10)
    return ' '.join(words)


def reset_test():
    global start_time, end_time, key_count, typing_speed
    global sentence
    sentence = generate_sentence()
    start_time = 0
    end_time = 0
    key_count = 0
    typing_speed = 0
    instructions.delete('1.0', 'end')
    instructions.insert('1.0', f'Type the following words:\n{sentence}')
    typing_speed_label.config(text=f'Typing speed = 0.00 characters per second')
    typing_accuracy_label.config(text=f'Typing accuracy = 0.00%')
    text_widget.delete('1.0', 'end')
    text_widget.bind('<KeyPress>', key_press)


def key_press(event):
    global start_time, end_time, key_count, typing_speed
    pressed_keys = {}
    if start_time == 0:
        start_time = time.time()
    key_count += 1
    pressed_keys[event.keysym] = True
    if event.keysym in pressed_keys:
        del pressed_keys[event.keysym]
        end_time = time.time()
        count_time()


def count_time():
    if start_time != 0:
        speed = (key_count / (end_time - start_time))
        typing_speed_label.config(text=f'Typing speed = {speed:.2f} characters per second')
        typing_accuracy_label.config(text=f'Typing accuracy = {accuracy():.2f}%')
        root.after(500, count_time)


def accuracy():
    typed_text = text_widget.get('1.0', 'end-1c')  # Get typed text without newline character
    # Ensure typed_text is as long as sentence to avoid index errors
    typed_text = typed_text[:len(sentence)]

    correct_chars = 0
    total_chars = 0

    # Compare each character in the sentence with the typed text
    for original_char, typed_char in zip(sentence, typed_text):
        if original_char != ' ':
            total_chars += 1
            if original_char == typed_char:
                correct_chars += 1

    if total_chars == 0:
        return 0
    return (correct_chars / total_chars) * 100


root = tk.Tk()
root.title('Key press detection')

sentence = generate_sentence()

instructions = tk.Text(root, wrap='word', height=10, width=50)
instructions.pack(padx=10, pady=10)
instructions.insert('1.0', f'type the following words:\n{sentence}')
text_widget = tk.Text(root, wrap='word', height=10, width=50)
text_widget.pack(padx=10, pady=10)
text_widget.bind('<KeyPress>', key_press)

typing_speed_label = tk.Label(root, text='Typing speed = 0.00 characters per second')
typing_speed_label.pack(padx=10, pady=10)
typing_accuracy_label = tk.Label(root, text='Typing accuracy = 0.00%')
typing_accuracy_label.pack(padx=10, pady=10)

restart_button = tk.Button(root, text='Restart', command=reset_test)
restart_button.pack()
root.after(500, count_time)
root.mainloop()
