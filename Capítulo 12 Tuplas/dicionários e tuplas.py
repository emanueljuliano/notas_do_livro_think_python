d = {'a':0, 'b':1, 'c':2}
t = d.items() #retorna uma sequência de tuplas
print(t)

for key, value in d.items():
    print(key, value)

t = [('a', 0), ('b', 1), ('c', 2)]
d = dict(t)
print(d)
#combinar dict e zip é mais fácil:
d = dict(zip('abc', range(3)))
print(d)

#update recebe uma lista de tuplas e as adiciona como par chave-valor
def telefone(last, first, number):
    directory = {}
    directory[last, first] = number
    for last, first in directory:
        print(first, last, directory[last, first])
