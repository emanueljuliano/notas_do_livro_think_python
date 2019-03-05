import math
import turtle

bob = turtle.Turtle()
alice = turtle.Turtle()

def polyline(t, n, lengh, angle):
    for i in range (n):
        t.fd(lengh)
        t.rt(angle)

def polygon(t, lengh, n):
    ang_ex = 360/n
    polyline(t, n, lengh, ang_ex)

polygon(bob, 100, 5)

def arc(t, r, arc):
    circunference = 2 * math.pi * r
    n_tot = int(circunference / 3) + 1
    lengh = circunference / n_tot
    n = int(n_tot * arc / 360)
    ang_ex = 360/n_tot
    polyline(t, n, lengh, ang_ex)

arc(alice, 100, 100)

turtle.mainloop()
