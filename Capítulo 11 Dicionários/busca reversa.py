def histogram(h):
    d = dict()
    for k in h:
        d[k] = d.get(k, 0) + 1
    return d
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

h = histogram('parrot')
k = reverse_lookup(h, 1)
print(k)
