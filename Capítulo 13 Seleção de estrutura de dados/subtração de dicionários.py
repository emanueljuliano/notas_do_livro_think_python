import string

def process_file(filename):
    hist = {}
    fin = open(filename)
    for line in fin:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.whitespace + string.punctuation)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1
    return hist

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def subtract_conjuntes(d1, d2):
    return set(d1) - set(d2)


words = process_file('words.txt')
hist = process_file('emma.txt')
diff = subtract(hist, words)
diff_conjuntes = subtract_conjuntes(hist, words)
print('Words in the book that aren´t in the word list: ')
for word in diff_conjuntes:
    print(word, end=' ')

