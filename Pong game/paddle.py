from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.setpos(paddle)

    def up(self):
        y_pos = self.ycor()
        self.penup()
        self.goto(self.xcor(), y_pos + 20)

    def down(self):
        y_pos = self.ycor()
        self.penup()
        self.goto(self.xcor(), y_pos - 20)

