from time import time
finn = open('words.txt')
lista = []
for line in finn:
    word = line.strip()
    lista.append(word)
    if len(lista) > 10000:
        break
lista.append('beshrews')
def has_duplicates(t):
    c = t
    n = 0
    for i in c:
        n += 1
        if i in c[n:]:
            return True
    return False

start = time()
print(has_duplicates(lista))
demora = time() - start
print(demora)