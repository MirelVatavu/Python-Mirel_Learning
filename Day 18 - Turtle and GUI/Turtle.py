import turtle
from turtle import Turtle, Screen, colormode
import random
import colorgram


colors = colorgram.extract('hirst2.jpg', 30)

n = 0
colors_list = []
for color in range (len(colors)):
    new_colors = colors[n]
    rgb = new_colors.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    s = (red, green, blue)
    n += 1
    colors_list.append(s)

print(colors_list)
tim = Turtle()
tim.shape('arrow')
tim.color('black')
# tim.speed = 0
#
# tim.pencolor('blue')
# tim.forward(200)
# tim.right(90)
# tim.pencolor('red')
# tim.forward(200)
# tim.right(90)
# tim.pencolor('green')
# tim.forward(200)
# tim.right(90)
# tim.pencolor('red')
#
# for _ in range(0,10):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

# Triangle
# print(tim.pos())
# tim.penup()
# tim.goto(0,200)
# tim.pendown()

colours = ['forest green', 'green yellow','crimson','medium slate blue','dark violet','gold','cyan','lime','pale turquoise','medium spring green','dark cyan']

## Drawing shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.pencolor(random.choice(colours))
#     draw_shape(shape_side_n)

# Drawing a Random Walk
tim.speed(0)
grades = [0,90,180,270]
colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
# for _ in range(0,1000):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(grades))
#     tim.forward(15)
#     tim.pensize(random.randint(0,10))

step_y = -400
tim.pensize(4)
tim.penup()
tim.goto (-700,step_y)
tim.pendown()
tim.hideturtle()
def moving_forward():
    for _ in range(10):
        tim.color(random.choice(colors_list))
        tim.dot(20,random.choice(colors_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

for _ in range(10):
    moving_forward()
    step_y += 50
    tim.penup()
    tim.goto(-700, step_y)
    tim.pendown()

tim.penup()
tim.goto (0,0)
tim.pendown()







def draw_spirograph(step):
    for _ in range (int(360/step)):
        tim.pencolor(random.choice(colors_list))
        tim.circle(100)
        tim.setheading(tim.heading()+ step)

draw_spirograph(10)













screen = Screen()
screen.exitonclick()
