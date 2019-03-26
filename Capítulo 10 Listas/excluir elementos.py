t = ['a', 'b', 'c']
x = t.pop(1) #exclui e retorna um elemento
print(t)
print(x)
del t[1] #somente exclui
print(t)
t.remove('a') #exclui um elemento sem precisar saber o índice
print(t)
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)