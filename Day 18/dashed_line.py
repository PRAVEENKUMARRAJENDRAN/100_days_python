from turtle import Turtle, Screen

t = Turtle()

for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
s = Screen()
s.exitonclick()