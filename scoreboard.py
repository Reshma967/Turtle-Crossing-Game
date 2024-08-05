from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1

    def over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align='center')

    def leve(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"LEVEL {self.level}", font=FONT, align='center')

    def inc(self):
        self.level+=1
        self.leve()







