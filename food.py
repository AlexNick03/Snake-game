from turtle import Turtle
import random

list_of_colors = ["red", "orange", "yellow", "green", "blue", "violet"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color(random.choice(list_of_colors))
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x_val = random.randint(-260, 260)
        random_y_val = random.randint(-260, 260)
        self.goto(random_x_val, random_y_val)
        self.color(random.choice(list_of_colors))
