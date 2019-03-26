import turtle

class Point:
    '''ponto'''

class Rectangle:
    '''retangulo'''

class Circle:
    '''circulo'''

roda = Circle()
roda.radius = 100
roda.center = Point()
roda.center.x = -100
roda.center.y = -100

pandora = Rectangle()
pandora.width = 100
pandora.heigth = 200
pandora.corner = Point()
pandora.corner.x = 100.0
pandora.corner.y = 100.0

tortuga = turtle.Turtle()
tortuga.pu()
tortuga.fd(pandora.corner.x)
tortuga.lt(90)
tortuga.fd(pandora.corner.y)
tortuga.rt(90)
tortuga.pd()
for i in range(2):
    tortuga.fd(pandora.width)
    tortuga.lt(90)
    tortuga.fd(pandora.heigth)
    tortuga.lt(90)

turtle.mainloop()