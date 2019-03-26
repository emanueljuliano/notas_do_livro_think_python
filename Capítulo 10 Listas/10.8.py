import random
def has_duplicated(t):
    c = t
    n = 0
    for i in c:
        n += 1
        if i in c[n:]:
            return True
    return False

def random_bdays(n):
    t = []
    for x in range(n):
        t.append(random.randint(1, 366))
    return t

def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        if has_duplicated(random_bdays(num_students)):
            count += 1
    return count

print(count_matches(23, 1000) / 1000)