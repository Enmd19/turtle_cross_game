import time
from turtle import Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard

scoreboard = Scoreboard()
speed = STARTING_MOVE_DISTANCE
cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
screen.listen()
screen.onkey(key="Up", fun=timmy.move_forward)
game_is_on = True
while game_is_on:
    car = CarManager()
    cars.append(car)
    for vehicle in cars:
        vehicle.move(speed=speed)
        time.sleep(0.1)
        screen.update()

    if timmy.ycor() > 275:
        timmy.move_to_the_beginning()
        speed += MOVE_INCREMENT
        scoreboard.add_point()
        for vehicle in cars:
            vehicle.hideturtle()
        cars.clear()

    else:
        for vehicle in cars:
            if vehicle.distance(timmy) < 27:
                scoreboard.game_over()
                game_is_on = False
screen.exitonclick()
