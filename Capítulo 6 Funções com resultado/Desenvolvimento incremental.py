from math import sqrt
def distance(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    disquared = dx**2 + dy**2
    result = sqrt(disquared)
    return result

print(distance(1, 2, 4, 6))