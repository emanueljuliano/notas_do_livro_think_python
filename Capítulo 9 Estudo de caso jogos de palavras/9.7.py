def cosecutives(word, n):
    if n == 3:
        return True
    if len(word) < 2:
        return False
    if word[0] == word[1]:
        return cosecutives(word[2:], n+1)
    return cosecutives(word[1:], 0)

#tambem pode ser:
def searched_word(word):
    count = 0
    index = 0
    while index < len(word)-1:
        if word[index] == word[index+1]:
            count +=1
            if count ==3:
                return True
            index += 2
        else:
            count = 0
            index += 1

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if searched_word(word):
        print(word)

