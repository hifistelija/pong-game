from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turn off animation

# Create the paddles
STARTING_POSITION_LEFT = (-350, 0)
STARTING_POSITION_RIGHT = (350, 0)

right_paddle = Paddle(STARTING_POSITION_RIGHT)
left_paddle = Paddle(STARTING_POSITION_LEFT)

# Create the ball and scoreboard
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
# Bind the keys for the right paddle
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
# Bind the keys for the left paddle
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

# Main game loop
is_game_on = True
while is_game_on:
    screen.update() # refresh the screen
    time.sleep(ball.move_speed)
    ball.move()

    # Check for collision with the top or bottom screen boundaries
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or\
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses and score left
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.point_left()

    # Detect if left paddle misses and score right
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.point_right()

screen.exitonclick()
