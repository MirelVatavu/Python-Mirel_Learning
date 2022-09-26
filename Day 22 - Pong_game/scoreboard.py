from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,positionX,positionY):
        super().__init__()
        self.penup()
        self.goto(positionX,positionY)
        self.hideturtle()
        self.color('Red')
        self.pendown()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.write(f'{self.score}', align='center', font=('Arial', 30, 'normal'))

    def score_increase(self):
        self.clear()
        self.score += 1
