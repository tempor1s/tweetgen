from itertools import permutations
from sys import argv
from dictionary_words import get_set_words_from_file
from utils import time_it


def get_anagram(s):
    # Return a list of all character permutations with a given word.
    # TODO: Make this return a single real word from dictonary
    return set([''.join(perm) for perm in permutations(s)])

@time_it
def get_real_anagram(s):
    anagrams_variations = get_anagram(s)
    words = get_set_words_from_file('/usr/share/dict/words')

    return anagrams_variations.intersection(words)
    # real_words = []
    # for word in words:
    #     if word in anagrams_variations:
    #         real_words.append(word)
    
    # # 150ms slower
    # # for word in anagrams_variations:
    # #     if word in words:
    # #         real_words.append(word)

    # return real_words


if __name__ == '__main__':
    args = argv[1:3]
    anagrams = get_real_anagram(args[0])
    print(anagrams)