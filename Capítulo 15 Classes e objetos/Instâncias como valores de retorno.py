class Point:
    '''point in the 2 dimensional space'''

class Rectangle:
    '''rectangle with width, height and corner'''

caixinha = Rectangle()
caixinha.width = 100.0
caixinha.height = 200.0
caixinha.corner = Point()
caixinha.corner.x = 0.0
caixinha.corner.y = 0.0

def print_point(p):
    print(f'({p.x}, {p.y})')

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(caixinha)
print_point(center)
