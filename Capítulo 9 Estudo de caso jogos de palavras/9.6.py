def is_abecedarian(word):
    letter = word[0]
    for i in word:
        if letter > i:
            return False
        letter = i
    return True

fin = open('words.txt')
n = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        n += 1
        print(word)
print(n)