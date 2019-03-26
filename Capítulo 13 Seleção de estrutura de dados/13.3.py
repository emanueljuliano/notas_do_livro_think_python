import string

def skip_gutemberg_head(fp):
    for line in fp:
        if line.startswith('  _VOLUME I._'):
            break

def retirar_sinais_proibidos(s):
    s = s.strip().lower()
    t = list(s)
    new = ''
    for i in t:
        if i not in string.punctuation:
            new = new + i
    return new

def hist(filename, skip_head):
    d = {}
    fin = open(filename)
    if skip_head:
        skip_gutemberg_head(fin)
    for line in fin:
        frase = retirar_sinais_proibidos(line)
        words = frase.split()
        for word in words:
            d[word] = d.get(word, 0) + 1
    return d

def most_freq(d):
    t = []
    for key, value in d.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t

def print_most_freq(hist, num=20):
    t = most_freq(hist)
    for freq, word in t[:num]:
        print(word, '\t', freq)


hist = hist('livro.txt')
print_most_freq(hist, 20)



