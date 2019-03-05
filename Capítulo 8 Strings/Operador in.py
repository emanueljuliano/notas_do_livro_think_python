#retorna True

print('a' in 'banana')
print('seed' in 'banana')

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('banana', 'abracadabra')