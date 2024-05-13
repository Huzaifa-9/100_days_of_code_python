from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)



