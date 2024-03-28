from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.level_up()

    def level_up(self):
        self.goto(-290, 250)
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(-0, 0)
        self.write("GAME OVER", align="center", font=FONT)
