from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_move_distance = 5
move_increase = 10

class Cars:
    def __init__(self):
        self.all_cars = []
        self.move_distance = start_move_distance

    def create_cars(self):
        if random.randint(1, 6) == 1:  # Control the frequency of car creation
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += move_increase
