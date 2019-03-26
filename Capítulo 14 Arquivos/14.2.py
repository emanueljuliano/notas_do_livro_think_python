import anagram_sets
import shelve


def store_anagrams(filename, anagram_map):
    prateleira = shelve.open(filename, 'c')

    for word, anagrams in anagram_map.items():
        prateleira[word] = anagrams

    prateleira.close()

def read_anagrams(word, arquivo):
    sig = anagram_sets.signature(word)
    anagramas = shelve.open(arquivo)
    try:
        return anagramas[sig]
    except KeyError:
        print('Palavra não encontrada')

def main():
    anagram_map = anagram_sets.all_anagrams('words.txt')
   # store_anagrams('funciona', anagram_map)
    print(read_anagrams('task', 'prateleira'))

if __name__ == '__main__':
    main()