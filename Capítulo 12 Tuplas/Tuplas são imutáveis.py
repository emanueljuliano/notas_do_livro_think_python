#lista de valores separados por vírgula
t = 'a', 'b', 'c', 'd', 'e' #pode ou não ter parêntese
print(t)
t1 = 'a', #tupla de um elemento precisa de vírgula
print(t1)
t = tuple()
print(type(t))
t = tuple('lupins')
print(t)
print(t[0])
print(t[1:3])
# t[0] = 'A' -> erro, tuplas não podem ser alteradas
t = ('A',) + t[1:]
print(t)
#operadores relacionais:
print((0, 1, 2) < (0, 3, 4))
print((0, 1, 2000000000000000000000000000000000) < (0, 3, 4))
lista = [1, 2, 3, 4]
