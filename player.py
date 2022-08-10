from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280
HEAD_NORTH = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(HEAD_NORTH)
        self.goto(STARTING_POSITION)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def check_finish(self):
        if self.ycor() >= FINISH_LINE:
            self.goto(STARTING_POSITION)
            return True
        return False
        