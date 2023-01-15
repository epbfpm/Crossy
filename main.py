from vehicles import *
from turtle import Screen
from player import Player
from ui import *

# screen parameters
screen = Screen()
screen.screensize(600, 600, 'gray10')
screen.colormode(255)
screen.title('Cross the road: NEGO DRAMA EDITION')
screen.listen()
screen.tracer(0)

# ui
sidewalk_top = Sidewalk_up(270)
sidewalk_middle = Sidewalks(1)
sidewalk_bottom = Sidewalks(-270)
border = Border()
lanes = Lanes()
score = Score()
game_over = GameOver()

# player
player = Player()


delay = 0
game_on = True
while game_on:
    delay += 1
    countdown = Countdown()
    if delay < 91:
        countdown.run(delay)
    elif delay == 91:
        car = Car()
        car.ini_spd()
    else:
        # movement
        screen.onkeypress(player.u, "Up")
        # screen.onkeypress(player.d, "Down")
        screen.onkeypress(player.l, "Left")
        screen.onkeypress(player.r, "Right")
    screen.update()
    car = Car()

    # level increase
    if player.ycor() > 240:
        score.refresh()
        car.refresh()
        player.refresh()

    # vehicle collision
    # for vehicle in car_list:
    #     if player.distance(vehicle) <= 20:
    #         game_over.show()
    #         game_on = False

screen.exitonclick()
