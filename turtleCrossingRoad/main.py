import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()


screen.onkeypress(player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_cars()
    car_manager.move_car()

    # detect Collision With Car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # reach the end wall
    if player.ycor() > 280:
        player.start_again()
        scoreboard.increase_scoreboard()
        car_manager.level_up()

    screen.update()

screen.exitonclick()
