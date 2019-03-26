#zip recebe duas ou mais sequencias e devolve uma lista de tuplas contendo um elemento de cada sequência
#zip é um iterador

s = 'abc'
t = [0, 1, 2]
print(zip(s, t))

for pair in zip(s, t):
    print(pair)

print(list(zip(s, t)))
print(list(zip('Anne', 'Elk')))

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)

def has_match(t1,t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

for index, element in enumerate('abc'):
    print(index, element)