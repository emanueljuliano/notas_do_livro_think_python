from time import time
finn = open('words.txt')
lista = []
for line in finn:
    word = line.strip()
    lista.append(word)
lista.append('tempest')
def has_duplicate(t):
    d = {}
    for i in t:
        if i in d:
            return True
        d[i] = 0
    return False
start = time()
print(has_duplicate(lista))
demora = time() - start
print(demora)