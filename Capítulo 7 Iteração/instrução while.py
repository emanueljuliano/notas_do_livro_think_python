def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print('Blatoff!')

countdown(10)

def Collatz_conjecture(n):
    while n != 1:
        print(n)
        if n % 2 == 0:    #n é par
            n = n/2
        else:             #n é impar
            n = n*3 + 1

Collatz_conjecture(11)