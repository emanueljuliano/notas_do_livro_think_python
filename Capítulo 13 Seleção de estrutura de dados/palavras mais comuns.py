import string

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t

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



hist = process_file('emma.txt')
t = most_common(hist)
print('The most common words are: ')
for freq, word in t[:40]:
    print(word, freq, sep='\t') #deixa a segunda coluna alinhada verticalmente