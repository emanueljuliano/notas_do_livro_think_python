eng2sp = dict()
print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
print(len(eng2sp))
print('one' in eng2sp) #in só funciona para chaves
print('uno' in eng2sp) #in não funciona para valores

vals = eng2sp.values() # retorna os valores
print(vals)
print('uno' in vals)