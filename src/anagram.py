from itertools import permutations
from sys import argv

def get_anagram(s):
    # Return a list of all character permutations with a given word.
    # TODO: Make this return a single real word from dictonary
    return sorted(set([''.join(perm) for perm in permutations(s)]))


if __name__ == '__main__':
    args = argv[1:3]
    anagrams = get_anagram(args[0])
    print(anagrams)