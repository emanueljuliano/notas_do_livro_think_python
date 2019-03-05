
def print_four_times(f):
    print(f)
    print(f)
    print(f)
    print(f)

def grade1():
    borda = ('+ ' + '- '*4)*2 + '+'
    meio = ('|         |         |')
    print(borda)
    print_four_times(meio)
    print(borda)
    print_four_times(meio)
    print(borda)

grade1()

def grade2():
    borda = ('+ ' + '- '*4) * 4 + '+'
    meio = '|         |         |         |         |'
    print(borda)
    print_four_times(meio)
    print(borda)
    print_four_times(meio)
    print(borda)
    print_four_times(meio)
    print(borda)
    print_four_times(meio)
    print(borda)

grade2()
