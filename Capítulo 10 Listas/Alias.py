a = [1, 2, 3]
b = a #associação = referência
print(b is a)
#objeto com mais de uma referência = Alias

b[0] = 42 #alterações em um alias afetam o outro
print(a)
