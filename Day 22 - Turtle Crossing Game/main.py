from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time
screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
player = Player()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(player.up,'Up')

game_on = True




car = Car()


car.add_car(50)

while game_on:
    screen.listen()
    screen.onkey(player.up, 'Up')

    screen.update()
    time.sleep(scoreboard.time)
    car.move()


    for each_car in car.cars:
        if each_car.distance(player.pos()) < 25:
            game_on = False

    if player.ycor() >270:
        screen.update()
        scoreboard.level()
        player.reset()
        car.reset()
    if game_on == False:
        answer = screen.textinput('Restart','Want to restart? Type Y').lower()
        if answer == 'y':
            player.reset()
            scoreboard.reset()
            car.reset()
            game_on = True
    car.regenerate()


screen.update()
screen.exitonclick()