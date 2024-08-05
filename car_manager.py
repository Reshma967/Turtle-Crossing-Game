from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        self.cars = []
        self.speed=STARTING_MOVE_DISTANCE

    def create(self):
        i = random.randint(1,6)

        if i==1:
            sel=Turtle()
            sel.shape("square")
            sel.penup()
            sel.shapesize(1,2)
            sel.color(random.choice(COLORS))
            y=random.randint(-250,250)
            sel.goto(300,y)
            self.cars.append(sel)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def inc(self):
        self.speed+=MOVE_INCREMENT