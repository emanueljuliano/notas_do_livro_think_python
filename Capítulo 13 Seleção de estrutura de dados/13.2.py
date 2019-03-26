fin = open('livro.txt')
import string
palavras_proibidas = string.whitespace + string.punctuation
frase = ''
def remove_things(s):
    palavras_proibidas = string.whitespace + string.punctuation
    new = s.strip().lower()
    for item in palavras_proibidas:
        new = new.replace(item, '')
    return new

def print_book(book):
    a = ''
    for line in book:
        if a == 'oi':
            print(remove_things(line), end='')
        if remove_things(line) == 'thetempest':
            a = 'oi'

def count_book_words(book):
    a = False
    c = 0
    for line in book:
        if a:
            for item in line.split():
                if item not in palavras_proibidas:
                    print(item)
                    c += 1
        if remove_things(line) == 'thetempest':
                a = True
    return print(c)
count_book_words(fin)