
from paddles import Paddle
from ball import Ball
from scoreboard import Score
import time

ball = Ball()
pong_game = Paddle()
score_1 = Score()
score_2 = Score()
final_score = Score()


player_1_score = 0
player_2_score = 0

still_playing = True

# global player_1_score, player_2_score, still_playing
def show_score():
    score_1.refresh_score(score=player_1_score, align="left", x_heading=-200)
    score_2.refresh_score(score=player_2_score, align="right", x_heading=200)

players = pong_game.move_paddle()
def game_play():
    player_1 = players[0]
    player_2 = players[1]
    sleep_value = 0.1
    global player_1_score, player_2_score, still_playing
    # score_1.refresh_score(score=player_1_score, align="left", x_heading=-200)
    # score_2.refresh_score(score=player_2_score, align="right", x_heading=200)
    while still_playing:
        pong_game.my_screen.update()
        ball.refresh()
        show_score()
        time.sleep(sleep_value)

        if ball.ycor() > (pong_game.default_y / 2 - 20) or ball.ycor() < -(pong_game.default_y / 2 - 20):
            ball.bounce_wall()

        if (ball.distance(player_1) < 30 and ball.xcor() < -320) or (ball.distance(player_2) < 30 and ball.xcor() > 320):
            ball.bounce_paddle()
            if sleep_value - 0.005 < 0:
                sleep_value -= 0.005

        if ball.xcor() > (pong_game.default_x / 2):
            player_1_score += 1
            ball.reset_position()
            show_score()

        if ball.xcor() < -(pong_game.default_x / 2):
            player_2_score += 1
            ball.reset_position()
            show_score()

        if player_1_score + player_2_score == 11:
            still_playing = False
            ball.hideturtle()
            if player_1_score > player_2_score:
                winner = "Player 1"
            else:
                winner = "Player 2"
            final_score.game_over(winner)

game_play()
pong_game.my_screen.exitonclick()