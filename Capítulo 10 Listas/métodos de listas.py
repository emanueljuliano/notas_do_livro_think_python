t = ['a', 'b', 'c']
t.append('d') # adiciona termos na lista
print(t)
t1 = ['a', 'b', 'c']
t2 = ['e', 'd']
t1.extend(t2) # toma uma lista como argumento e adiciona
print(t1)

print(t1.sort()) #deveria deixar em ordem alfabética, mas só altera e retorna none
print(t1)
#sorted deixa em ordem alfabética e retorna uma nova lista