import random
import string

def correcao(s):
    new = ''
    letras_proibidas = string.punctuation + '“`‘’´”1234567890'
    frase = s.strip().lower()
    for letter in list(frase):
        if letter not in letras_proibidas:
            new += letter
    return new.split()

def process_file(filename, skip_head):
    dona_tromba = open(filename)
    if skip_head:
        skip_diegos_head(dona_tromba)
    d = {}
    t = []
    for line in dona_tromba:
        t.extend(correcao(line))
    for word in t:
        d[word] = d.get(word, 0) + 1
    return d

def skip_diegos_head(fp):
    for line in fp:
        if line.startswith('  _VOLUME I._'):
            break

def choose_from_hist(hist):
    t = []
    for key in hist:
        t.extend([key]*hist[key])
    return random.choice(t)

words = process_file('livro.txt', True)
print(choose_from_hist(words))
