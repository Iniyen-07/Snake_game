from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)


    def random_food(self):
        r_x = random.randint(-380, 380)
        r_y = random.randint(-380, 380)
        self.goto(r_x, r_y)
