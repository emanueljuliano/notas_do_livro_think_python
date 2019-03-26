import pprint
verbose = True
def example1():
    if verbose:
        print('Running example1')
example1()

#não é possível reatribuir vairáveis globais:
been_called = False
def example2():
    been_called = True

#A n ser que se especifíque que ela é global
count = 0
def example3():
    global count
    count += 1

#Ou ela seja mutável:
known = {0:0, 1:1}
def example4():
    known[2] = 1

#Mas para reatribuí-la, é preciso decralá-la:
def example5():
    global known
    known = dict()
