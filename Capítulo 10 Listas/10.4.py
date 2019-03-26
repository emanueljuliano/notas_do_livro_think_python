def chop(t):
    del t[0]
    del t[-1]

t = [1, 2, 3, 4]
chop(t)
print(t)
