from math import pi
def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if x == y:
            return y
        x = y
def factorial(a):
    if a == 0:
        return 1
    s = a * factorial(a - 1)
    return s
def estimate_pi():
    soma = 0
    i = 0
    while True:
        termo = (factorial(4*i) * (1103 + 26390*i) / (factorial(i)**4 * 396**(4*i)))
        soma += termo
        i += 1
        if termo <= 10 ** -15:
            break

    equacao = 2 * mysqrt(2) / 9801 * soma
    return 1 / equacao

print(estimate_pi())
print(pi)