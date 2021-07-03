from paddle import Paddle
from turtle import Screen
from ball import Ball
import time


screen = Screen()
screen.bgcolor('black')
screen.screensize(500,500)
screen.listen()
screen.tracer(0)


r_paddle = Paddle((310,0))
l_paddle = Paddle((-320,0))

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    if ball.ycor() == 270 or ball.ycor() == -270:
        ball.wall_bounce()
        print("BB")
    if r_paddle.distance(ball) < 50 and ball.xcor() == 300:
        ball.paddle_bounce()
        print("EE")
    if ball.distance(l_paddle) < 50 and ball.xcor() == -310:
        ball.paddle_bounce()
        print("PP")
    if ball.xcor() > 310 or ball.xcor() < -320:
        is_on = False
    ball.move_ball()

screen.exitonclick()
