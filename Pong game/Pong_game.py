import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
h = 600
w = 800
screen.screensize(w, h, "black")
screen.setup(w + 20, h + 20)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
# screen.onkey(ball.move, "space")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with a wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() > -320:
        ball.bounce_x()

    # detect when ball misses the R paddle
    if ball.xcor() > w/2:
        ball.reset_ball()
        score.score_disp_r()

    # detect when ball misses the L paddle
    if ball.xcor() < -w/2:
        ball.reset_ball()
        score.score_disp_l()

screen.exitonclick()
