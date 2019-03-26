#print('1'.zfill(2)) preenche a string com zeros à esquerda

def idades_palindromas(g, n, c, a):
    if a == 1 and c == 6:
        return print(g-1, n-1)
    if n > 100:
        return False
    if c == 8:
        return idades_palindromas(0, n-g, 0, 1)
    if str(g).zfill(2) == str(n).zfill(2)[::-1]:
        return idades_palindromas(g+1, n+1, c+1, a)
    return idades_palindromas(g+1, n+1, c, a)

for i in range (15, 99):
    idades_palindromas(0, i, 0, 0)


