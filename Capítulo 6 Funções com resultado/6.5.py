def gdc(a, b):
    r = a % b
    if r == 0:
        return print(f'GDC = {b}')
    gdc(b, r)

gdc(18, 12)