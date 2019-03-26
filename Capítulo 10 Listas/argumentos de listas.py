def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

''' letters e t são alias
    prestar atenção em operadores que alteram e criam novas listas
    a seguinte função não remove a cabeça de uma lista '''


def bad_delete_head(t):
    t = t[1:]


bad_delete_head(letters)
print(letters)


def tail(t):
    return t[1]


print(tail(letters))