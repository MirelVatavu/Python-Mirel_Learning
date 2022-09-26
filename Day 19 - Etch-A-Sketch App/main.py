import random
import turtle
from turtle import Turtle, Screen
is_race_on = False

screen = Screen()

# tim.speed(0)
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def rotate_right():
#     tim.setheading(tim.heading()-10)
#
# def rotate_left():
#     tim.setheading(tim.heading()+10)
#
# def angles():
#     tim.setheading(tim.heading()+90)
#
# def clear_drawing():
#     screen.resetscreen()
#
# screen.listen()
#
# screen.onkey(key='Up',fun=move_forward)
# screen.onkey(key='Down',fun=move_backward)
# screen.onkey(key='Right',fun=rotate_right)
# screen.onkey(key='Left',fun=rotate_left)
# screen.onkey(key='space',fun=angles)
# screen.onkey(key='c',fun=clear_drawing)
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title= "Bet", prompt = "Who will win? Insert a color: ").lower()

colors = ['red','orange','yellow','green','blue','purple','indigo']
y_pos = [-120, -80, -40, 0, 40, 80, 120]
all_turtles =[]

for turtle_index in range(0,7):
    new_turtle = Turtle(shape ='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_pos[turtle_index])
    new_turtle.speed(0)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()