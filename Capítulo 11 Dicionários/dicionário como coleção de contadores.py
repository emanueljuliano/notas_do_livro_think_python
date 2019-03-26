def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h)

h = {'a': 1}
print(h.get('a', 0)) #get retorna o valor correspondente da chave indicada
print(h.get('b', 0)) #se ela n existir, retorna o valor padrão

def new_histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

print(new_histogram('brontosaurus'))