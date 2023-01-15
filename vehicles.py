from turtle import Turtle
from random import randint, choice, uniform

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
