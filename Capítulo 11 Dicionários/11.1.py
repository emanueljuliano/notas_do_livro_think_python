import time
def dictionary(arquive):
    finn = open(arquive)
    n = 0
    d = dict()
    for line in finn:
        word = line.strip()
        n += 1
        d[word] = n
    return d

def word_hunter(word, dictionary):
    if word in dictionary:
        return True
    return False

d = dictionary('words.txt')
start = time.time()
print(word_hunter('tempest', d))
demora = time.time() - start
print(demora)