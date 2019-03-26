import string
import random
import sys

suffix_map = {}
prefix = ()

def process_file(filename, order=2):
    fp = open(filename)
    skip_gutenberg_head(fp)

    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)

def skip_gutenberg_head(fp):
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

def process_word(word, order=2):
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return
    try:
        suffix_map[prefix].append(word)
    except KeyError:
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)

def random_test(n = 100):
    start = random.choice(list(suffix_map.keys()))

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            random_test(n-i)
            return
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)

def shift(t, word):
    return t[1:] + (word,)

def main(script, filename='emma.txt', n=0, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage %d filename [# of words] [prefix length]' %script)
    else:
        process_file(filename, order)
        random_test(n)
        print()

if __name__ == '__main__':
    main(*sys.argv)

process_file('emma.txt')
random_test()
print(prefix)
print(suffix_map)

