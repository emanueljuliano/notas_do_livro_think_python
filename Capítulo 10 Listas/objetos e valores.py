a = 'banana'
b = 'banana'
print(a is b) #a e b são o mesmo objeto

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) #a e b não são o mesmo objeto, mas possuem o mesmo valor
print(a == b)