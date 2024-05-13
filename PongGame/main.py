from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_score_board = ScoreBoard((-100, 190))
r_score_board = ScoreBoard((100, 190))

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()

    # detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        l_score_board.score_write()
        ball.reset_position()

    elif ball.xcor() < -400:
        r_score_board.score_write()
        ball.reset_position()

    screen.update()

screen.exitonclick()
