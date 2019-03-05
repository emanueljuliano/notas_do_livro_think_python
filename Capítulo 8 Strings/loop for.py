fruit = 'banana'
index = -1
while index >= -len(fruit):
    letter = fruit[index]
    print(f'{letter}')
    index -= 1

prefixes = 'JKLMNOPQ'
sufix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        letter += 'u'
    print(letter + sufix)