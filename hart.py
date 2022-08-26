import turtle
t=turtle.Turtle()
t.speed(0.2)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)
def txt():
    t.color("pink","pink")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()
def write():
    t.up()
    t.setpos(-40,90)
    t.down()
    t.color("black")
    t.write("_vyankat_",font=("vardana",18,"bold"))
txt()
write()

input()

        
