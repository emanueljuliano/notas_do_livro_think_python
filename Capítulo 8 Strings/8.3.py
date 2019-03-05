fruit = 'banana'
print(fruit[0:6:2])
print(fruit[::-1])

def is_palindrome(word):
    if word == word[::-1]:
        print('É um palíndromo!')
    else:
        print('Não é um palíndromo!')

is_palindrome('kayak')