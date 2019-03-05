def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
    elif n < 0:
        print('Factorial is not defined for negative integers.')
    elif n == 0:
        print(space, 'returning 1')
        return 1
    else:
        result = n * factorial(n-1)
        print(space, 'returning', result)
        return result

factorial(4)
