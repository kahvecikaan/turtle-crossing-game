import time
import turtle as t
import player as p
import car_manager as c
import scoreboard as s

screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

player = p.Player()
car_manager = c.CarManager()
scoreboard = s.Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if player completes the level
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
