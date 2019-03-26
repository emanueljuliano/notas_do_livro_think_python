class Point:
    '''point'''

class Rectangle:
    '''rectangle'''

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

#mudando tamnaho sem mudar sua posição
box.width = box.width + 50
box.height = box.height + 100

def grow_rectangle(rect, dwidth, dheight):
    rect.width = rect.width + dwidth
    rect.height = rect.height + dheight

print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)

def move_rectangle(rect, dx, dy):
    rect.corner.x = rect.corner.x + dx
    rect.corner.y = rect.corner.y + dy

print(f'({box.corner.x}, {box.corner.y})')
move_rectangle(box, 13, 17)
print(f'({box.corner.x}, {box.corner.y})')
