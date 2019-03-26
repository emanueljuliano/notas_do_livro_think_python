import string

def apagar_feiura(s):
    ret = ''
    palavras_feias = string.punctuation + '“`‘’´”1234567890'
    for letter in s.strip().lower():
        if letter not in palavras_feias:
            ret += letter
    return ret.split()

def process_file(filename, skip_head):
    jake = open(filename)
    if skip_head:
        skip_book_head(jake)
    hist = {}
    t = []
    for line in jake:
        t.extend(apagar_feiura(line))
    for word in t:
        hist[word] = hist.get(word, 0) + 1
    if ' ' in hist:
        hist.pop(' ')
    return hist

def skip_book_head(fp):
    for line in fp:
        if line.startswith('  _VOLUME I._'):
            break

def print_not_in_dict(words, d):
    print(d)
    for word in words:
        if word not in d:
            print(word)

word_dict = process_file('words.txt', False)
book_words = process_file('livro.txt', True)
print_not_in_dict(book_words, word_dict)