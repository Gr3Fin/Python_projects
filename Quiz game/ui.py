# --- Create the user interface for the quiz ---

from tkinter import *
from tkinter import messagebox
from tweet import ScoreTweet
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # type declaration
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.window.attributes("-topmost", True)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125,
                                                text="",
                                                width=280,
                                                font=(FONT_NAME, 20, "italic"),
                                                fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, sticky="we")

        self.score_label = Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, sticky="e")
        self.q_info = Label(text="Category:", justify="left", fg="white", bg=THEME_COLOR)
        self.q_info.grid(row=0, column=0, sticky="w")

        ok = PhotoImage(file="images/true.png")
        no = PhotoImage(file="images/false.png")
        self.button_ok = Button(image=ok, command=self.yes_button, highlightthickness=0)
        self.button_no = Button(image=no, command=self.no_button, highlightthickness=0)
        self.button_ok.grid(row=2, column=0, sticky="w")
        self.button_no.grid(row=2, column=1, sticky='e')

        self.question_display()

        self.window.mainloop()

    def question_display(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text[0])
            self.q_info.config(text=f"Category: {q_text[1]},\nLevel: {q_text[2]}")
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text="THE END")
            self.button_ok.config(state="disabled")
            self.button_no.config(state="disabled")
            self.tweet_popup()

    def yes_button(self):
        is_true = self.quiz.check_answer("True")
        self.check_answer(is_true)

    def no_button(self):
        is_true = self.quiz.check_answer("False")
        self.check_answer(is_true)

    def check_answer(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.question_display)

    def tweet_popup(self):
        tweet = messagebox.askquestion(message="Would you like to share your quiz score on Twitter?")
        if tweet == "yes":
            tweet = ScoreTweet()
            tweet.tweet_score(score=self.quiz.score, q_no=self.quiz.question_number)
        self.window.destroy()
