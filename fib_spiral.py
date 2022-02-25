import turtle
s = turtle.Screen()
t = turtle.Turtle()

first = 0
sec = 1

for i in range(50):
    n = first
    first = sec
    sec = n + sec
    t.forward(1)
    t.circle(sec, 90)
