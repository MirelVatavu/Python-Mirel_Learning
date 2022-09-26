from turtle import Turtle,Screen
from pad import Pad
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=1200,height=800)
cut_screen = Turtle()
r_score = Scoreboard(30,350)
l_score = Scoreboard(-30,350)
ball = Ball()



cut_screen.color('white')
cut_screen.penup()
cut_screen.goto(0, -380)
cut_screen.setheading(90)
cut_screen.pensize(4)
cut_screen.hideturtle()
for _ in range(19):
    cut_screen.up()
    cut_screen.forward(20)
    cut_screen.pendown()
    cut_screen.forward(20)

screen.bgcolor('Black')

pad = Pad()


screen.listen()
screen.onkey(pad.up_two, 'Up')

screen.onkey(pad.down_two, 'Down')

screen.onkey(pad.up_one, 'w')

screen.onkey(pad.down_one, 's')


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 380 or ball.ycor() <-380:
        ball.bounce_y()
    if ball.distance(pad.l_pad) < 50 and ball.xcor() <-560 or ball.distance(pad.r_pad) < 50 and ball.xcor()>550:
        ball.bounce_x()

    # Right pad misses
    if ball.xcor() > 610:
        l_score.score_increase()
        l_score.show_score()
        ball.refresh()

    # Left pad misses
    if ball.xcor() < -610:
        r_score.score_increase()
        r_score.show_score()
        ball.refresh()
screen.exitonclick()