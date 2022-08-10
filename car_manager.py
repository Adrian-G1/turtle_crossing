from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_EDGE = 300
HEAD_WEST = 180

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(choice(COLORS))
        self.setheading(HEAD_WEST)
        self.shapesize(stretch_len=2)
        self.goto(x=SCREEN_EDGE, y=randint(-250, 250))
        self.starting_speed = STARTING_MOVE_DISTANCE
        
    
    def move(self):
        self.forward(self.starting_speed)