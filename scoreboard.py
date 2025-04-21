
from turtle import Turtle

player_1 = 0
player_2 = 0

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.t = Turtle()
        self.t.hideturtle()
        self.t.color("white")
        self.t.speed("fastest")
        self.t.penup()
        self.default_y = 600
        self.default_x = 600

    def refresh_score(self, score, align, x_heading):
        self.t.clear()
        self.t.goto(x=x_heading, y=(self.default_y/2 - 90))
        self.t.write(score,align=align, font=("Courier", 80, "normal"))

    def game_over(self, winner):
        self.t.goto(x=0, y=0)
        self.t.write(f"GAME OVER, The winner is {winner}",
                align="center", font=("Arial", 16, "bold"))

