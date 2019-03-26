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
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def most_common(hist):
    t = []
    for key, values in hist.items():
        t.append((values, key))
    t.sort(reverse=True)
    return t

def print_most_commom(hist, num=10):
    t = most_common(hist)
    print('The most common words are: ')
    for freq, word in t[:num]:
        print(word, freq, sep='\t\t')

hist = process_file('emma.txt')

print_most_commom(hist, 20)