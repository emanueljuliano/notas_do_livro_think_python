def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram('undertale', 'deltarune'))