from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('Highscore.txt', 'r') as file:
            self.highscore=int(file.read())
        self.color('Red')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.highscore}', align=ALIGNMENT, font=FONT)
        with open('Highscore.txt', 'w') as file:
            file.write(f'{self.highscore}')

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.updated_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg='GAME OVER.', align=ALIGNMENT, font=FONT)
    def score_increase(self):
        self.score = self.score + 1
        self.updated_scoreboard()




