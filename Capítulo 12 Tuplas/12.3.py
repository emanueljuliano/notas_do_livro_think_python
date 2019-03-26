from time import time
def par_metatese(t1, lista):
    count = 0
    for word in lista:
        for x, y in zip(t1, word):
            if x != y:
                count += 1
        if count == 2:
            print(t1, word)

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    d = {}
    marceline = open(filename)
    for line in marceline:
        word = line.strip()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

def all_pares_metateses(d):
    for anagrams in d.values():
        for i in range(len(anagrams) - 1):
            par_metatese(anagrams[i], anagrams[i+1:])


anagramas = all_anagrams('words.txt')
all_pares_metateses(anagramas)
