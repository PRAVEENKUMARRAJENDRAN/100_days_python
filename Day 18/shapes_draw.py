from turtle import Turtle, Screen

t = Turtle()

i = 3
while i < 10:
    for j in range(i):
        t.forward(100)
        t.right(360/i)
    i += 1


s = Screen()
s.exitonclick()