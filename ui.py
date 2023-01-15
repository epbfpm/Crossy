from turtle import Turtle


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
