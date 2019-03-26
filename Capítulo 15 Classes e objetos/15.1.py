import math
import copy

class Point:
    '''point'''

class Rectangle:
    '''rectangle'''

class Circle:
    '''circle with radius and a center object point'''

class Reta:
    '''reta ax + by + c = 0'''

def distance(p1, p2):
    distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return distance

def point_in_circle(circle, point):
    if distance(circle.center, point) <= circle.radius:
        return True
    else:
        return False

def rect_in_circle(circle, rect):
    p = copy.copy(rect.corner)
    if point_in_circle(circle, p):
        p.y = p.y + rect.heigth
        if point_in_circle(circle, p):
            p.x = p.x + rect.width
            if point_in_circle(circle, p):
                p.y = p.y - rect.heigth
                return point_in_circle(circle, p)
    return False

def make_r(p1, p2):
    r = Reta()
    if p1.y - p2.y == 0:
        r.a = 0.0
        r.b = 1
        r.c = - p1.y

    else:
        r.a = 1
        r.b = 0
        r.c = -p1.x
    return r

def distance_point_r(p, r):
    return abs(r.a*p.x + r.b*p.y + r.c) / math.sqrt(r.a**2 + r.b**2)

def rect_circle_overlap(circle, rect):
    retas = []
    p1 = copy.copy(rect.corner)
    p2 = copy.copy(rect.corner)
    p3 = copy.copy(rect.corner)
    p4 = copy.copy(rect.corner)
    p2.y = p3.y = p2.y + rect.heigth
    p3.x = p4.x = p3.x + rect.width
    retas.append(make_r(p1, p2))
    retas.append(make_r(p2, p3))
    retas.append(make_r(p3, p4))
    retas.append(make_r(p4, p1))
    for reta in retas:
        try:
            if distance_point_r(circle.center, reta) < circle.radius:
                return True
        except:
            return False
    return False


def main():
    #def circle
    circulin = Circle()
    circulin.radius = 100.0
    circulin.center = Point()
    circulin.center.x = 0.0
    circulin.center.y = 30.0

    #def point
    puntin = Point()
    puntin.x = 10.0
    puntin.y = 20.0

    #def rectangle
    pandora = Rectangle()
    pandora.width = 1000.0
    pandora.heigth = 2000.0
    pandora.corner = Point()
    pandora.corner.x = 10000.0
    pandora.corner.y = 10000.0

    print(rect_circle_overlap(circulin, pandora))

main()