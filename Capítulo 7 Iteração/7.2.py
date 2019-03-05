def eval_loop():
    n = ''
    while True:
        n = input('> ')
        if n == 'done':
            print(a)
            break
        a = n
        print(eval(a))

eval_loop()