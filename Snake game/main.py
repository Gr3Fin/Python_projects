# The main file that executes the game

import snake
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

# Initiate screen
screen = Screen()
screen.listen()
w = h = 600
screen.setup(w, h)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food collision
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_disp()

    # detect wall collision
    if (snake.segments[0].xcor() > w/2-20 or snake.segments[0].xcor() < -(w/2-20) or snake.segments[0].ycor() > h/2-20
            or snake.segments[0].ycor() < -(h/2-20)):
        scoreboard.reset_hs()
        snake.reset_snake()
        # game_on = False
        # scoreboard.game_over()

    # detect tail collision
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset_hs()
            # game_on = False
            # scoreboard.game_over()

screen.exitonclick()
