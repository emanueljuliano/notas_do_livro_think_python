def read_dictionary(filename='pronunce_dict.txt'):
    d = dict()
    finn = open(filename)
    for line in finn:
        if line[0] == '#': continue
        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def word_hunter(word, dictionary):
    if word in dictionary:
        return True
    return False

def homofonos(word, dictionary):
    word2 = word[1:]
    if word_hunter(word2, dictionary) and dictionary[word2] == dictionary[word]:
        word3 = word[0] + word[2:]
        if word_hunter(word3, dictionary) and dictionary[word3] == dictionary[word]:
            print(word, word2, word3)

d = read_dictionary()

for word in d:
    homofonos(word, d)


