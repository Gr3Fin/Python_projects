# Handle credentials for tweeting the quiz score

from tkinter import *
from tkinter import messagebox

from tweet import ScoreTweet
from quiz_brain import QuizBrain


class LogInInfo:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Twitter login...")
        self.window.config(pady=20, padx=20, background="white")

        canvas = Canvas(width=200, height=200, highlightthickness=0, background="white")
        logo_img = PhotoImage(file="images/twitter_s.png")
        canvas.create_image(100, 100, image=logo_img)
        canvas.grid(row=0, column=1, columnspan=3)

        web_label = Label(text="User name:")
        web_label.grid(row=1, column=0)
        web_label = Label(text="e-mail:")
        web_label.grid(row=2, column=0)
        web_label = Label(text="Password:")
        web_label.grid(row=3, column=0)

        self.user_in = Entry(width=50)
        self.user_in.grid(row=1, column=1, columnspan=3)
        self.user_in.focus()
        self.mail_in = Entry(width=50)
        self.mail_in.grid(row=2, column=1, columnspan=3)
        self.pass_in = Entry(width=50, show='*')
        self.pass_in.grid(row=3, column=1, columnspan=3)
        self.cred = ()

        x_button = Button(text="Share", command=self.share)
        x_button.grid(row=4, column=1)
        save_button = Button(text="Save", command=self.save)
        save_button.grid(row=4, column=2)
        load_button = Button(text="Load", command=self.load)
        load_button.grid(row=4, column=3)

        self.window.mainloop()

    def save(self):
        self.cred = self.user_in.get(), self.mail_in.get(), self.pass_in.get()
        if not all(self.cred):
            messagebox.showinfo(title="Oops..", message="You've left some empty fields!")
        else:
            is_ok = messagebox.askokcancel(message=f"Details entered: \nUser name: {self.cred[0]} "
                                                   f"\nemail: {self.cred[1]} \nPassword: {self.cred[2]}")
            if is_ok:
                with open('login_data.txt', mode="w") as file:
                    file.write(f"{self.cred[0]}\n{self.cred[1]}\n{self.cred[2]}\n")

    def load(self):
        self.user_in.delete(0, END)
        self.mail_in.delete(0, END)
        self.pass_in.delete(0, END)
        try:
            with open("login_data.txt") as file:
                login = file.readlines()
        except FileNotFoundError:
            messagebox.showinfo(message="There is no file with login data.")
        else:
            self.user_in.insert(0, login[0].strip())
            self.mail_in.insert(0, login[1].strip())
            self.pass_in.insert(0, login[2].strip())


    def share(self):
        self.cred = self.user_in.get(), self.mail_in.get(), self.pass_in.get()
        if not all(self.cred):
            messagebox.showinfo(title="Oops..", message="You've left some empty fields!")
        else:
            tweet = ScoreTweet()
            tweet.tweet_score(score=self.quiz.score, q_no=self.quiz.question_number, cred=self.cred)
            self.window.destroy()
