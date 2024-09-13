from turtle import Turtle, Screen, colormode
from random import *

t = Turtle()
t.speed("fastest")

colormode(255)

for _ in range(1000):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.circle(50)

    


s = Screen()
s.exitonclick()