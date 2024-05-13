from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(self.score, align="center", font=("courier", 88, "normal"))

    def score_write(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("courier", 88, "normal"))
