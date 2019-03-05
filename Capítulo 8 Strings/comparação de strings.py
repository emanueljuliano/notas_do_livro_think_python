word = 'banana'
if word == 'banana':
    print('All righ, bananas.')

word = 'banan'
if word < 'banana': #possível deixar em ordem alfabética
    print(f'Your word, {word}, comes before banana.')
elif word > 'banana':
    print(f'Your word, {word}, comes after banana.')
else:
    print('All righ, bananas.')

#todas as letras maiúsculas vem antes de todas as letras minúsculas
