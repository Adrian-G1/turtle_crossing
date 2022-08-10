from turtle import Turtle

FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-290, y=270)
        self.update_level()
        
    def update_level(self):
        self.write(arg=f"Level: {self.level}", font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
        
    def game_over(self):
        self.home()
        self.write(arg='GAME OVER', align='center', font=FONT)