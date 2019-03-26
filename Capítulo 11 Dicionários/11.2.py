def make_word_dict(arquive):
    d = dict()
    n = 0
    jake = open(arquive)
    for line in jake:
        word = line.strip()
        d[word] = n
        n += 1
    return d

def invert_dict(d):
    invert = {}
    for key in d:
        val = d[key]
        invert.setdefault(val, []).append(key)
    return invert

d = invert_dict(make_word_dict('words.txt'))
print(d)
print(len(d))