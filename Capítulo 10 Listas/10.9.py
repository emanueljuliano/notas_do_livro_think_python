import time

def make_word_list1():
    t1 = []
    finn = open('words.txt')
    for line in finn:
        word = line.strip()
        t1.append(word)
    return t1

def make_word_list2():
    t2 = []
    jake = open('words.txt')
    for line in jake:
        word = line.strip()
        t2 += [word]
    return t2

start_time = time.time()
t1 = make_word_list1()
elapsed_time = time.time() - start_time
print(len(t1))
print(t1[:10])
print(elapsed_time)

start_time2 = time.time()
t2 = make_word_list2()
elapsed_time2 = time.time() - start_time2
print(len(t2))
print(t2[:10])
print(elapsed_time2)