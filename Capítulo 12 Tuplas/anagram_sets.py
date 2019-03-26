def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    d = {}
    marceline = open(filename)
    for line in marceline:
        word = line.strip()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

def print_anagrams_sets(d):
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)

def print_anagrams_sets_in_order(d):
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))
    t.sort(reverse=True)
    for c in t:
        print(c)

def filter_lenght(d, n):
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res

if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    print(print_anagrams_sets_in_order(anagram_map))


    eight_letters = filter_lenght(anagram_map, 8)
    print_anagrams_sets_in_order(eight_letters)