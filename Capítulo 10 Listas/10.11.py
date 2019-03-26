import bisect

def make_word_list():
    t = []
    jake = open('words.txt')
    for line in jake:
        word = line.strip()
        t.append(word)
    return t

def is_palindrome(word):
    return word == word[::-1]

def in_bisect(word_list, word):
    x = bisect.bisect_left(word_list, word)
    if x == len(word_list):
        return False
    return word_list[x] == word

def par_inverso(word_list, word):
    if not is_palindrome(word):
        inv = word[::-1]
        return in_bisect(word_list, inv)
    return False

word_list = make_word_list()

for word in word_list:
    if par_inverso(word_list, word):
        print(word, word[::-1])


