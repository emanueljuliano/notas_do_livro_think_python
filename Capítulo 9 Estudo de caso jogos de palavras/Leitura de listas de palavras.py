fin = open('words.txt')
print(fin.readline())
print(fin.readline()) #objeto grava a posição em que estava no arquivo
line = fin.readline()
word = line.strip()
print(word)

for line in fin:
    word = line.strip()
    print(word)