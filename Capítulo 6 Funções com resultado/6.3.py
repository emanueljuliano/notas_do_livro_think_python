def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1: -1]
def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        print('A palavra é um palindromo.')
    elif first(word) == last(word):
        is_palindrome(middle(word))
    else:
        print('A palavra não é um palindromo.')

is_palindrome('kayak')