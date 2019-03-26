import bisect

def make_wordlist():
    t = []
    finn = open('words.txt')
    for line in finn:
        word = line.strip()
        t.append(word)
    return t

def in_bisect(word_list, word):
    x = bisect.bisect_left(word_list, word)
    if x == len(word_list):
        return False
    return word_list[x] == word

def interligam(word_list, word):
    even = word[::2]
    odd = word[1::2]
    return in_bisect(word_list, even) and in_bisect(word_list, odd)

def interligam_geral(word_list, word, n):
    for i in range(n):
        a = word[i::n]
        if not in_bisect(word_list, a):
            return False
    return True

word_list = make_wordlist()
for word in word_list:
    if interligam_geral(word_list, word, 3):
        print(word, word[0::3], word[1::3], word[2::3])
