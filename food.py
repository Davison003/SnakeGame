from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('red')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.rand_pos()

    def rand_pos(self):
        self.setpos(random.randint(-270, 270), random.randint(-270, 270))
