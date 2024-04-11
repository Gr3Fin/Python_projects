# --- Create the quiz app that displays 10 random questions (True/False) from different categories. ---

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
from tweet import ScoreTweet

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_category = question["category"]
    question_lvl = question["difficulty"]
    new_question = Question(question_text, question_answer, question_category, question_lvl)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

tweet = ScoreTweet()
tweet.tweet_score(score=quiz.score, q_no=quiz.question_number)
