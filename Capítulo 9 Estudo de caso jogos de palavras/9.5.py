def uses_all(word, list):
    for i in list:
        if i not in word:
            return False
    return True

fin = open('words.txt')
n = 0
for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiouy'):
        n += 1
        print(word)
print(n)
