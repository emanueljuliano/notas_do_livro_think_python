def uses_only(word, list):
    for l in word:
        if l not in list:
            return False
    return True

fin = open('words.txt')

for line in fin:
    word = line.strip()
    if uses_only(word, 'acefhlo'):
        print(word)
