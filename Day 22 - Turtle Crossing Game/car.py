from turtle import Turtle
import random
COLORS = ['red','green','yellow','purple']
Y_POS = [-240,-200,-160,-120,-80,-40,0,40,80,120,160,200,240]
class Car():
    def __init__(self):
        self.cars = []


    def add_car(self,cars):
        for new_car in range(0,cars):
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.randint(120,1000), random.choice(Y_POS))
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.forward(10)

    def regenerate(self):
        for car in range(0,len(self.cars)):
            if self.cars[car].xcor() < -330:
                new_car = Turtle('square')
                new_car.color(random.choice(COLORS))
                new_car.penup()
                new_car.goto(random.randint(300, 600), random.choice(Y_POS))
                new_car.setheading(180)
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                self.cars.append(new_car)
                self.cars[car].hideturtle()
                self.cars.remove(self.cars[car])

            else:
                pass

    def reset(self):
        for car in range(0,len(self.cars)):
            self.cars[car].hideturtle()
            self.cars.remove(self.cars[car])
            self.add_car(1)