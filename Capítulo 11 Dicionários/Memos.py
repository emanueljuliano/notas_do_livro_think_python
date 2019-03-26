#memo = dicionário que guarda valores para não executar a função várias vezes

known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print(fibonacci(990)) #caraca é mto mais rápido