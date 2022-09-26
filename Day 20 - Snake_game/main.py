from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake by Kazuky')
screen.tracer(0)
# Create a snake body

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()
game_is_on = True


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')



while game_is_on:
    screen.update()

    time.sleep(0.06)
    snake.move(10)
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_increase()
        snake.extend()
    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<7:
            scoreboard.reset()
            snake.reset()

    # if head collides with any segment in the tail
        # trigger game_over

    print(scoreboard.score)
screen.exitonclick()
