from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for items in question_data:
    text = items["question"]
    answer = items["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.ask_question()
    if quiz.question_number == len(question_bank):
        print(f"You have completed the quiz. Your final score is {quiz.score}/{len(question_bank)}")