from turtle import Turtle, Screen
import random
COLORS = ['red','green','yellow','purple']
screen = Screen()
car = Turtle()

new_cars = []
for new_car in range(10):
    new_car = car.shape('square')
    new_car = car.color(random.choice(COLORS))
    new_car = car.penup()
    new_car = car.goto(300, random.randint(40,500))
    new_car = car.setheading(180)
    new_car = car.shapesize(stretch_wid=0.5, stretch_len=random.randint(1, 3))
    new_cars.append(new_car)

print(new_cars)

screen.exitonclick()