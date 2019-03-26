import math
class Point:
    '''cria um ponto em um espaço bidimensional'''

blank = Point()
blank.x = 3.0
blank.y = 4.0

white = Point()
white.x = 6.0
white.y = 8.0



print(f'({blank.x}, {blank.y})')
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)

def print_point(p):
    print(f'({p.x}, {p.y})')

print_point(blank)

def distance_between_point(p1, p2):
    distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    print(distance)

distance_between_point(blank, white)
