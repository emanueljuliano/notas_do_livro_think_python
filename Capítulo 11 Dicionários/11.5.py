def make_word_dict():
    fiona = open('words.txt')
    d = {}
    for line in fiona:
        word = line.strip()
        d[word] = None

    return d

def rotate_word(word, n):
    new_word = ''
    for c in word:
        num = ord(c) + n
        new_word += chr(num)

    return new_word

def pares_rotacionados(word, word_dict):
    for n in range(1, 14):
        rotated = rotate_word(word, n)
        if rotated in word_dict:
               print(word, n, rotated)

word_dict = make_word_dict()
for word in word_dict:
    pares_rotacionados(word, word_dict)




