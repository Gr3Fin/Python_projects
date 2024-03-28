from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.color("white")
        self.score_count_l = score
        self.score_count_r = score
        self.score_disp_l()

    def score_disp_l(self):
        self.clear()
        self.write(f"{self.score_count_l} : {self.score_count_r}", align=ALIGNMENT, font=FONT)
        self.score_count_l += 1

    def score_disp_r(self):
        self.clear()
        self.write(f"{self.score_count_l} : {self.score_count_r}", align=ALIGNMENT, font=FONT)
        self.score_count_r += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
