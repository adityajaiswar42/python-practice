import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(1)
turtle.shapesize(2)
t.color("cyan","green")
t.fillcolor("orange")
t.begin_fill
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
turtle.done()
turtle.input()