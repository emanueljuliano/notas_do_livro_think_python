import math
def area(radius):
    return math.pi * radius**2

def absolut_value(x):
    if x < 0:
        return -x
    else:
        return x

#python tem uma função integrada chamada abs que retorna valores absolutos

def comparador(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

print(comparador(3, 2))