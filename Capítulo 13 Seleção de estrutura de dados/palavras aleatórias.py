import bisect
import random
import string
import time

def process_file(filename):
    h = {}
    fiona = open(filename)
    for line in fiona:
        process_line(line, h)
    return h

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word]*freq)
    return random.choice(t)

def real_random_word(h):
    freqs = []
    words = []
    total_freq = 0
    for word, freq in h.items():
        total_freq += freq
        freqs.append(total_freq)
        words.append(word)
    x = random.randint(0, total_freq -1)
    index = bisect_search(freqs, x)

    return words[index]

def bisect_search(t, item):
    return bisect.bisect_left(t, item)

hist = process_file('emma.txt')
start1 = time.time()
print(real_random_word(hist))
tempo1 = time.time() - start1
print(tempo1)
start2 = time.time()
print(random_word(hist))
tempo2 = time.time() - start2
print(tempo2)


