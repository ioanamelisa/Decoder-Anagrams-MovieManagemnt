from itertools import permutations

def read_dictionary(dictionary_path):
    with open(dictionary_path, 'r') as dictionary_file:
        return set(word.strip().lower() for word in dictionary_file.readlines())

def generate_anagrams(word):
    return set(''.join(permutation) for permutation in permutations(word))

def find_meaningful_anagrams(word, dictionary_path):
    dictionary_words = read_dictionary(dictionary_path)
    anagrams = generate_anagrams(word)
    meaningful_anagrams = set(filter(lambda anagram: anagram in dictionary_words, anagrams))
    return meaningful_anagrams