# import turtle
#
# jimmy = turtle.Turtle()
# print(jimmy)
# jimmy.shape("turtle")
# jimmy.color("DarkOrange2")
# jimmy.turtlesize(stretch_wid=5)
# my_screen = turtle.Screen()
# jimmy.pencolor("coral")
# jimmy.forward(-300)
# jimmy.forward(600)
# jimmy.forward(-300)
# jimmy.right(-90)
# jimmy.forward(300)
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water"," Fire"])

table.align = 'l'


print(table)