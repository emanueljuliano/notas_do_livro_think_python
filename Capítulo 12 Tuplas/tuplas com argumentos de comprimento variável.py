def printall(*args): # * permite atribuir uma quantidade variável de argumentos, reunindo-os
    print(args)

printall(1, 2.0, '3', True)

t = (7, 3)
#divmod(t) -> erro, pois precisa de 2 argumentos
print(divmod(*t)) # * também pode dividir, caso usado em uma tupla

def sumall(*t):
    n = 0
    for i in t:
        n += i
    return n

print(sumall(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
