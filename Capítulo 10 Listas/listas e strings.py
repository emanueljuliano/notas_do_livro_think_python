s = 'spam'
s2 = 'i love you :3'
t = list(s) #quebra em letras
c = s2.split() #quebra em palavras
print(t)
print(c)

s = 'spam-spam-spam'
delimiter = '-'
print(s.split(delimiter))

t = ['i', 'love', 'you', ':3']
delimiter = ' '
s = delimiter.join(t) #concatena elementos de uma lista, mas é um método de string
print(s)




def cat():
    cat = open('cat.txt')
    for line in cat:
        print(f'{line}', end= '')
