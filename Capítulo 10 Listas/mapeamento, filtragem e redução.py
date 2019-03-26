#somar todos os elementos de uma lista
def add_all(t): #redução
    total = 0
    for x in t:
        total += x
    return total
nums = [1, 2, 3, 4, 5]
print(add_all(nums))
print(sum(nums)) # função integrada que soma os elementos

def capitalize_all(t): #mapeamento
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

palavras = ['Qual', 'a', 'resposta', 'para', 'a', 'vida', 'a', 'verdade', 'e', 'tudo', 'mais', '?']
print(capitalize_all(palavras))

def only_upper(t):   #filtragem
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper(capitalize_all(palavras)))