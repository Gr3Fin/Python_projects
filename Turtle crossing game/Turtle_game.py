import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
# speedup = 0.1

while game_is_on:
    # time.sleep(speedup)
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    # detect collision with car
    for n in car.all_cars:
        if player.distance(n) < 20:
            level.game_over()
            game_is_on = False

    # detect crossing the road
    if player.ycor() > 290:
        player.reset_turtle()
        # speedup *= 0.5
        car.speedup()
        level.level_up()


screen.exitonclick()
