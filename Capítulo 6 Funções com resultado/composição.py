from math import sqrt, pi

def distance(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    disquared = dx**2 + dy**2
    result = sqrt(disquared)
    return result

def area(radius):
    area = pi * radius**2
    return area

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

print(circle_area(1, 2, 4, 6))