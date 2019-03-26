import bisect
import time
def make_word_list():
    finn = open('words.txt')
    t = []
    for line in finn:
        words = line.strip()
        t.append(words)
    return t

Sorted_list = make_word_list()

def in_bisect(t, word):
    if len(t) == 0:
        return False

    metade = len(t)//2
    if t[metade] == word:
        return True

    if word < t[metade]:
            return in_bisect(t[:metade], word)
    else:
            return in_bisect(t[metade:], word)

def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    return word_list[i] == word

start1 = time.time()
print(in_bisect(make_word_list(), 'tempest'))
demora1 = time.time() - start1
start2 = time.time()
print(in_bisect_cheat(make_word_list(), 'tempest'))
demora2 = time.time() - start2
print(demora1)
print(demora2)