from random import randint
from turtle import Screen
from time import sleep
from types import new_class
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True

while game_on:
    sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move()
    
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_on = False
            score.game_over()
        
    if player.check_finish():
        score.increase_level()
        car_manager.increase_speed()


screen.exitonclick()