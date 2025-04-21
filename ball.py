
from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=-0.7, stretch_wid=-0.7)
        self.color("white")
        self.speed("slowest")
        self.refresh()


    def refresh(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddle()

