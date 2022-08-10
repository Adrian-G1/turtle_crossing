from turtle import Screen
from time import sleep
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True

while game_on:
    sleep(0.1)
    screen.update()
    car.move()
    
    if player.distance(car) < 30:
        game_on = False
        score.game_over()
    


screen.exitonclick()