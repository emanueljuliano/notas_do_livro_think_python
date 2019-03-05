for i in range (100):
    d = i*3 + 1
    c = d*3 / 2 + 1
    b = c*3 / 2 + 1
    a = b * 3 / 2 + 1
    if a % 1 == b % 1 == c % 1 == d % 1 == 0:
        print(i, d, c, b, a)

