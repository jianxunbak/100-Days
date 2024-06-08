from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("arial", 20, "italic")
FONT_1 = ("arial", 10, "bold")


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # ----WINDOW---- #
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(pady=30, padx=20, bg=THEME_COLOR)

        # ----IMAGE---- #
        false = PhotoImage(file="./images/false.png")
        true = PhotoImage(file="./images/true.png")

        # ----CANVAS---- #
        self.main_canvas = self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 124,
                                                     text="blah",
                                                     font=FONT,
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # ----BUTTON---- #
        self.right_button = Button(image=true, highlightthickness=0, border=0, command=self.true_press)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=false, highlightthickness=0, border=0, command=self.false_press)
        self.wrong_button.grid(row=2, column=1)

        # ----Label----#
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=FONT_1)
        self.score.grid(row=0, column=1)

        # ----NEXT QUESTION----#
        self.get_next_question()

        # ----MAINLOOP----#
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reach the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true_press(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
