def nested_sum(t):
    n = 0
    for i in t:
        if type(i) == list:
            n += nested_sum(i)
        else:
            n += i
    return n


t = [[1, [2]], [3], [4, 5, 6]]
print(nested_sum(t))
