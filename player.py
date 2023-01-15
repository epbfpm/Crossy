from turtle import Turtle


STEP = 30


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

