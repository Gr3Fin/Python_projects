# Crate and control the snake
from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Create a class that controls the snake
class Snake:

    def __init__(self):
        self.segments = []

        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")  # 20x20 pix size
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    # Add a new segment to the snake's tail
    def extend(self):
        self.add_segment(self.segments[-1].position())  # -1 start counting from the end of the list
        # position() is a Turtle function that returns the position of a turtle

    #  Make the snake move towards
    def move(self):

        for seg in range(len(self.segments) - 1, 0, -1):  # for loop in reverse direction start, stop, step
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    # Control the snake by using up, left, right arrows on the keyboard
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
