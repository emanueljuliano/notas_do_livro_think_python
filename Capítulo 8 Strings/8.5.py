#ord -> transforma letra em número
#chr -> transforma número em letra
def rotate_world(word, n):
    new_word = ''
    for c in word.lower():
        num = ord(c) + n
        if num > 122:
            num -= 26
        elif num < 97:
            num += 26
        new_word += chr(num)
    return new_word

print(rotate_world('emanuel', 13))