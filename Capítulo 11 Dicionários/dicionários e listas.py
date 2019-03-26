def histogram(h):
    d = dict()
    for c in h:
        d[c] = d.get(c, 0) + 1
    return d
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
hist = histogram('parrot')
invert = invert_dict(hist)
print(invert)

#listas podem ser valores mais não chaver
t = [1, 2, 3]
d = dict
#d[t] = 'oops'
# print(d) erro