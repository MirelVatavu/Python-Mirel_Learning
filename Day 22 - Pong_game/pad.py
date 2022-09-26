from turtle import Turtle
STARTING_POSITIONS = [(-580,0),(570,0)]
UP = 90
DOWN = 270
class Pad():
    def __init__(self):
        self.segments = []
        self.create_pad()
        self.l_pad = self.segments[0]
        self.r_pad = self.segments[1]

    def create_pad(self):
        for position in STARTING_POSITIONS:
            self.new_segment(position)

    def new_segment(self,position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color('White')
        new_segment.shapesize(1,5)
        new_segment.setheading(90)
        self.segments.append(new_segment)

    def up_one(self):
        self.l_pad.setheading(UP)
        self.l_pad.forward(20)

    def down_one(self):
        self.l_pad.backward(20)

    def up_two(self):
        self.r_pad.setheading(UP)
        self.r_pad.forward(20)

    def down_two(self):
        self.r_pad.backward(20)