from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1, outline=0)
            random_y = random.randint(-260, 260)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            # car.backword(STARTING_MOVE_DISTANCE)
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.car_speed += 10










