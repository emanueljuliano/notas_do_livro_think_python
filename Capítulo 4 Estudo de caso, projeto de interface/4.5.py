import math
import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.color("red")

def espiral_de_arquimedes(t, voltas):
    r = 1
    t.lt(90)
    for i in range (180*voltas):
        t.fd(r/100)
        t.lt(2)
        r += 1
espiral_de_arquimedes(bob, 15)

turtle.mainloop()
