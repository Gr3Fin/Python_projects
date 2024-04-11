# --- Create the quiz app that displays 10 random questions (True/False) from different categories. ---
from tkinter import messagebox

from question_model import Question
from data import QuizData #question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


def play_again():
    next_round = messagebox.askquestion(message="Would you like to play again?")
    if next_round == "yes":
        return True
    else:
        return False


play = True

while play:
    question_bank = []
    q_data = QuizData()
    for question in q_data.question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        question_category = question["category"]
        question_lvl = question["difficulty"]
        new_question = Question(question_text, question_answer, question_category, question_lvl)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    play = play_again()
