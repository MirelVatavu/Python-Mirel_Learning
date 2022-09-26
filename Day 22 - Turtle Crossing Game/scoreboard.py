from turtle import Turtle
LEVEL = 1
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.time = 0.1
        self.write_level()


    def write_level(self):
        self.clear()
        self.color('Red')
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.write(f'Level: {LEVEL}', align='left', font=('Arial', 20, 'normal'))

    def level(self):
        global LEVEL
        LEVEL += 1
        self.time *= 0.9
        self.write_level()

    def reset(self):
        global LEVEL
        LEVEL = 1
        self.time = 0.1
        self.write_level()