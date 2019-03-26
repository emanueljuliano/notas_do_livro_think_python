cache = {}
def ackerman(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackerman(m-1, 1)
    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackerman(m-1, ackerman(m, n-1))
        return cache[m, n]

print(ackerman(3, 8))