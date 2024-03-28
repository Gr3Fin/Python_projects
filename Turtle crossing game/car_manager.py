from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:      # generate fewer cars, every time 1 is chosen
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.starting_pos_y = random.choice(range(-240, 240, 20))
            new_car.starting_pos_x = random.choice(range(340, 380, 20))
            new_car.goto(new_car.starting_pos_x, new_car.starting_pos_y)
            self.all_cars.append(new_car)

    def speedup(self):
        self.car_speed += MOVE_INCREMENT

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

