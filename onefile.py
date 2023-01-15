from random import randint, choice
from turtle import Turtle, Screen

STEP = 30
spd = 2
increment = 0
car_list = []


class Car:
    def __init__(self):
        self.ran_col = (randint(50, 200), randint(50, 200), randint(50, 200))
        self.y_list = [225, 195, 165, 135, 105, 75, 45, -45, -75, -105, -135, -165, -195, -225]
        self.y = choice(self.y_list)
        self.create()
        self.move()
        self.remove()

    def create(self):
        global car_list
        global spd
        global increment
        if spd - 1 % 3 == 0 and spd < 13:
            increment = int(spd/3)
        if randint(0, 30) % (5 - increment) == 0:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.color(randint(50, 200), randint(50, 200), randint(50, 200))
            new_car.color()
            new_car.shapesize(1, 2)
            if self.y < 0:
                new_car.setpos(-280, self.y)
                new_car.setheading(0)
            else:
                new_car.setpos(280, self.y)
                new_car.setheading(180)

            self.car_distance(new_car)

    def car_distance(self, xcar):
        x = True
        if len(car_list) > 0:
            for car in car_list:
                if xcar.distance(car) < 70 and xcar.ycor() == car.ycor():
                    xcar.hideturtle()
                    x = False
        if x:
            car_list.append(xcar)

    def move(self):
        for car in car_list:
            car.forward(spd)

    def remove(self):
        for car in car_list:
            if abs(car.xcor()) >= 280:
                car.hideturtle()
                car_list.remove(car)

    def refresh(self):
        global spd
        spd += 0.5

    def ini_spd(self):
        global spd
        spd = 2

class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.setpos(0, -20)

    def run(self, t):
        if 30 > t >= 1:
            self.write(arg=f'3', font=('Arial', 30, 'normal'))
        if 60 > t >= 30:
            self.clear()
            self.write(arg=f'2', font=('Arial', 30, 'normal'))
        if 90 > t >= 60:
            self.clear()
            self.write(arg=f'1', font=('Arial', 30, 'normal'))
        if t == 90:
            self.clear()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.setpos(-285, 282)
        self.level = 0
        self.refresh()

    def refresh(self):
        self.level += 1
        self.clear()
        self.write(arg=f'Level: {self.level}', font=('Arial', 12, 'normal'))


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.setpos(-75, -15)

    def show(self):
        self.clear()
        self.write(arg=f'GAME OVER', font=('Arial', 20, 'normal'))


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-302, 302)
        self.pensize(4)
        self.color('black')
        self.pendown()
        self.goto(-302, -302)
        self.goto(303, -302)
        self.goto(303, 302)
        self.goto(-302, 302)


class Sidewalk_up(Turtle):
    def __init__(self, mod):
        super().__init__()
        self.penup()
        self.color('chartreuse4')
        self.setpos(0, 260)
        self.shape('square')
        self.shapesize(2, 30)


class Sidewalks(Turtle):
    def __init__(self, mod):
        super().__init__()
        self.penup()
        self.color('chartreuse4')
        self.setpos(0, mod)
        self.shape('square')
        self.shapesize(3, 30)


class Lanes(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('gray50')
        for sign in [1, -1]:
            for lanes in range(6):
                y = 210 * sign - lanes * 30 * sign
                self.setpos(-295, y)
                self.pensize(2)
                for spaces in range(0, 30):
                    self.pendown()
                    self.setx(self.xcor() + 10)
                    self.penup()
                    self.setx(self.xcor() + 10)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('orange')
        self.shapesize(0.8)
        self.penup()
        self.setheading(90)
        self.setpos(0, -255)

    def u(self):
        self.sety(self.ycor() + STEP)

    def d(self):
        self.sety(self.ycor() - STEP)

    def l(self):
        if (self.xcor() - STEP) < -270:
            self.setx(-270)
        else:
            self.setx(self.xcor() - STEP)

    def r(self):
        if (self.xcor() + STEP) > 270:
            self.setx(270)
        else:
            self.setx(self.xcor() + STEP)
        print(self.pos())

    def refresh(self):
        self.setpos(0, -255)
# screen parameters
screen = Screen()
screen.screensize(600, 600, 'gray10')
screen.colormode(255)
screen.title('Cross the jaca: NEGO DRAMA EDITION')
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
    for vehicle in car_list:
        if player.distance(vehicle) <= 20:
            game_over.show()
            game_on = False

screen.exitonclick()
