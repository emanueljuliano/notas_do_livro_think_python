def print_point(p):
    print(f'({p.x}, {p.y})')

class Point:
    '''point'''

class Rectangle:
    '''rectangle'''

box = Rectangle()
box.width = 100.0
box.heigth = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

p1 = Point()
p1.x = 3.0
p1.y = 4.0
import copy
p2 = copy.copy(p1)
print_point(p1)
print_point(p2)
print(p1 is p2) #não são o mesmo objeto
print(p1 == p2) #para instâncias, comportamente de == é igual ao de is

box2 = copy.copy(box) #cópia superficial -> copia objeto e qualquer referência, mas não objetos integrados
print(box2 is box)
print(box2.corner is box.corner) #corner é o mesmo em ambos

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner) #box 3 e box são objetos completamente separados

def move_rectangle(rect, dx, dy):
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x = new_rect.corner.x + dx
    new_rect.corner.y = new_rect.corner.y + dy
    return new_rect

print(f'({box3.corner.x}, {box3.corner.y})')
box4 = move_rectangle(box3, 123, 321)
print(f'({box4.corner.x}, {box4.corner.y})')