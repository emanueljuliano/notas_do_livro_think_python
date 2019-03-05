epsilon = 0.0000000001
a = 5
x = 4
while True:
    print(x)
    y = (x + a/x) / 2
    if abs(y - x) < epsilon:
        break
    x = y
