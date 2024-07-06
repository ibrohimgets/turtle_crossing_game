import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create player, cars, and scoreboard instances
player = Player()
cars = Cars()
scoreboard = Scoreboard()

# Keybinding for player movement
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

# Main game loop
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # Create and move cars
    cars.create_cars()
    cars.move_cars()

    # Detect collision with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if player reached the finish line
    if player.finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase()

screen.exitonclick()
