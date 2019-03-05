from math import sqrt

def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if x == y:
            return y
        x = y

mysqrt(3)

def test_square_root(a):
    space = '   '
    i = 1
    print('a  mysqrt(a)    math.sqrt(a) diff')
    print('-  --------     -----------  ----')
    while i <= a:
        print(f'{i:.1f} {mysqrt(i):.8f}  {sqrt(i):.8f}   {abs(mysqrt(i) - sqrt(i))}')
        i += 1

test_square_root(15)