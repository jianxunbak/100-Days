from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(TIMER)
    timer_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="LONG BREAK", fg=PINK)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="SHORT BREAK", fg=RED)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            mark = "✔"
            tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato)
timer_text = canvas.create_text(125, 150, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), width=5, bg=YELLOW, fg=GREEN, highlightthickness=0,
                      command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), width=5, bg=YELLOW, fg=GREEN, highlightthickness=0,
                      command=reset_time)
reset_button.grid(column=3, row=3)

tick_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
tick_label.grid(column=2, row=3)

window.mainloop()
