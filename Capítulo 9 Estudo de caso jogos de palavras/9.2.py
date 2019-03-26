def has_no_e(word):
    if word.count('e') == 0:
        return True
    else:
        return False

fin = open('words.txt')
tot = 0
no_e = 0
for line in fin:
    tot += 1
    word = line.strip()
    if has_no_e(word):
        no_e += 1
        print(word)
        
print(f'O total de palavras é {tot}, o número de palavras sem ´e´ é {no_e} e sua porcentagem é {no_e*100/tot:.4}%')

