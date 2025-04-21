
from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self):
        """Initializing screen attributes"""
        super().__init__()
        self.my_screen = Screen()
        self.my_screen.title("Pong!!!")
        self.default_x = 800
        self.default_y = 600
        self.my_screen.setup(width=self.default_x, height=self.default_y)
        self.my_screen.bgcolor("black")
        self.my_screen.tracer(0)
        self.paddle_1 = []
        self.paddle_2 = []
        self.x_pos = (self.default_x/2)-20
        self.player_1 = (-(self.x_pos + 10), 0)
        self.player_2 = (self.x_pos, 0)


    def create_players(self):
        """Creating pong paddle per player"""
        t = self.create_paddle(self.player_1)
        self.paddle_1.append(t)

        t = self.create_paddle(self.player_2)
        self.paddle_2.append(t)

    def create_paddle(self, position):
        t = Turtle(shape="square")
        t.shapesize(stretch_wid=3, stretch_len=1)
        t.color("white")
        t.penup()
        t.goto(position)
        return t

    def move_paddle(self):
        self.create_players()
        player_1 = self.paddle_1[0]
        player_2 = self.paddle_2[0]


        def move_up():
            new_y = player_1.ycor() + 20
            player_1.goto(player_1.xcor(), new_y)

        def move_down():
            new_y = player_1.ycor() - 20
            player_1.goto(player_1.xcor(), new_y)

        def up():
            new_y = player_2.ycor() + 20
            player_2.goto(player_2.xcor(), new_y)

        def down():
            new_y = player_2.ycor() - 20
            player_2.goto(player_2.xcor(), new_y)

        self.my_screen.listen()
        self.my_screen.onkey(move_up, "w")
        self.my_screen.onkey(move_down, "s")
        self.my_screen.onkey(up, "Up")
        self.my_screen.onkey(down, "Down")


        return player_1, player_2