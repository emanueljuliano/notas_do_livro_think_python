import matplotlib.pyplot as plt
from math import log
import string

#log f = log c - s log r
# f = frequência, r = classificação

def process_file(filename):
    h = {}
    finn = open(filename)
    skip_head(finn)
    for line in finn:
        process_line(line, h)
    return h

def skip_head(finn):
    for line in finn:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

def process_line(line, h):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        h[word] = h.get(word, 0) + 1

def sort_frequence_words(h):
    t = []
    num = []
    count = 0
    for key, value in h.items():
        count += 1
        t.append(log(value))
        num.append(log(count))
    t.sort(reverse=True)
    plt.plot(t, num)
    plt.show()



hist = process_file('emma.txt')


sort_frequence_words(hist)
