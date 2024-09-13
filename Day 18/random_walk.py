from turtle import Turtle, Screen, colormode
from random import *

t = Turtle()
t.pensize(20)
directions = [0, 90, 180, 270]
t.speed("fastest")

colormode(255)


for _ in range(1000):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.forward(30)
    t.setheading(choice(directions))
    


s = Screen()
s.exitonclick()