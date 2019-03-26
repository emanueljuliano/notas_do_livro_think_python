def make_histogram(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) +1
    return d

def read_file(filename):
    return open(filename).read()

def most_frequent(s):
    hist = make_histogram(s)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    return res

text = read_file('português.txt')
print(most_frequent(text))