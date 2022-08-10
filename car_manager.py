from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
SCREEN_EDGE = 300
HEAD_WEST = 180

class CarManager():
    def __init__(self):
        self.cars = []
        self.starting_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        if randint(1, 6) == 6:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.color(choice(COLORS))
            car.setheading(HEAD_WEST)
            car.shapesize(stretch_len=2)
            car.goto(x=SCREEN_EDGE, y=randint(-250, 250))
            self.cars.append(car)
            
    
    def move(self):
        for car in self.cars:
            car.forward(self.starting_speed)
        
    def increase_speed(self):
        self.starting_speed += MOVE_INCREMENT