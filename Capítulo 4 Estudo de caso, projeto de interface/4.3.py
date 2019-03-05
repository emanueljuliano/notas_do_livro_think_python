import math
import turtle
bob = turtle.Turtle()

def casco_de_tortuga (t, lados):
    ang_int = 360 / lados
    ang_ext = 180 - (180 - ang_int)/2
    lengh_int = 100
    lengh_ext = lengh_int / math.sin((180 - ang_int)/2 * math.pi / 180) * math.sin(ang_int * math.pi / 180)
    t.lt(30)
    for i in range (lados):
        t.fd(lengh_int)
        t.lt(ang_ext)
        t.fd (lengh_ext)
        t.lt(ang_ext)
        t.fd(lengh_int)
        t.lt(180)
    print(lengh_ext)

casco_de_tortuga (bob, 9)



turtle.mainloop()
