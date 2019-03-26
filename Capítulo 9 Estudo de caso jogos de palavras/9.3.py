def avoids(word, list):
    for l in word:
        if l in list:
            return False
    return True

listona = input('Digite letras para verificar o número de palavras que não as possui: ')
list = listona.lower().strip()

fin = open('words.txt')
n = 0
for line in fin:
    word = line.strip()
    if avoids(word, list):
        n += 1
print(f'Existem {n} palavras sem nenhuma das letras {list}')
