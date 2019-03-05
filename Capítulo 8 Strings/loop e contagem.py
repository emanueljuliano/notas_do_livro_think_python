def count(word, letter, index):
    count = 0
    for letra in word[index:]:
        if letra == letter:
            count += 1
    print(count)

count('abracadabra', 'b', 1)