import math
import turtle
bob = turtle.Turtle()
bob.color("red", "")
bob.speed(0)

def polyline(t, n, lengh, angle):
    for i in range(n):
        t.fd(lengh)
        t.lt(angle)

def arc(t, r, angle):
    arc_lengh = 2 * math.pi * r * angle / 360
    n = int(arc_lengh / 3) + 1
    step_lengh = arc_lengh / n
    step_angle = angle / n
    polyline(t, n, step_lengh, step_angle)

def petala(t, r, angle):
    for i in range (2):
        arc(t, r, angle)
        t.lt(180-angle)

def flor(t, n, r, angle):
    for i in range (n):
        petala(t, r, angle)
        t.lt(360/n)

flor (bob, 12, 300, 40)

turtle.mainloop()
