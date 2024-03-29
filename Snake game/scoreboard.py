# Create a scoreboard

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # now Score class can do everything as Turtle class
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.score_count = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.score_disp()   # refer to the score_disp function below when the object is created

    def score_disp(self):
        self.clear()
        self.write(f"Score: {self.score_count} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.score_count += 1

    def reset_hs(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            self.keep_score()
        self.score_count = 0
        self.score_disp()

    def keep_score(self):
        with open("highscore.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
