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
        self.score_disp()   # refer to the score_disp function below when the object is created

    def score_disp(self):
        self.clear()
        self.write(f"Score: {self.score_count}", align=ALIGNMENT, font=FONT)
        self.score_count += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
