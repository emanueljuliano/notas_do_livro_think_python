n = 'spam'
def do_twice(f, n):
    f(n)
    f(n)

def print_twice(a):
    print(a)
    print(a)

def do_four(x, y, z):
    x(y, z)
    x(y, z)

do_four(do_twice, print_twice, n)
