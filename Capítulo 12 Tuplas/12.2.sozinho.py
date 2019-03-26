def signature(word):
    t = list(word)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    d = {}
    fiona = open(filename)
    for line in fiona:
        word = line.strip()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

def print_anagrams_sets_in_order(d):
    t = []
    for anagrams in d.values():
        if len(anagrams) > 1:
            t.append((len(anagrams), anagrams))
    t.sort(reverse=True)
    for set in t:
        print(set)

anagrams_map = all_anagrams('words.txt')
print_anagrams_sets_in_order(anagrams_map)