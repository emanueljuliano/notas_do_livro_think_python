def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
def print_hist(h):
    for c in h:
        print(c, h[c])


h = histogram('parrot')
print_hist(h)
print('------------------')
for key in sorted(h):
    print(key, h[key])
