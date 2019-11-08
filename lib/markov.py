from dictogram import Dictogram
from utils import get_clean_words
from random import choice


class MarkovChain(dict):
    def __init__(self, word_list):
        super().__init__() # Initialize this as a new dict

        # Check to make sure a word list is passed in
        if word_list:
            for i in range(0, len(word_list)):
                # The current word in the iteration
                word = word_list[i]
                
                try:
                    # The word 1 index ahead of the current word, aka the next word in the sentence
                    # has to be in try except because of index out of range exception on end of list
                    next_word = word_list[i + 1]
                # If index error then no new words in list to add so break out    
                except IndexError:
                    break

                # The word dictogram if it exists
                word_dicto = self.get(word, None)

                if word_dicto is not None:
                    # Add a new word entry to the dictogram if the dictogram already exists
                    word_dicto.add_count(next_word, 1)
                else:
                    # Create a new dictogram for the word
                    self[word] = Dictogram([next_word])

    def sample(self, word):
        """
        Gets a random word from the histogram with the word as key

        Params:
            word: str - The word you want to sample from
        """
        histo = self.get(word, None)

        if histo:
            return histo.sample(1)
        else:
            raise Exception('Invalid word')
    
    def walk(self, count=10):
        # Get a random starting word from the self keys
        next_word = choice(list(self.keys()))
        # Start a list with the 'starting' word as the first entry
        words = [next_word]
        # Loop count - 1 times through the list to 'walk' through states
        for _ in range(0, count - 1):
            # Sample the next word and then get it as a string as sample returns a list
            next_word = self.sample(next_word)[0]
            # Append that word to the 'words' list and then move on to next iteration with new state
            words.append(next_word)
        # Return the list of words
        return words



if __name__ == "__main__":
    words = get_clean_words('txt_files/sherlock.txt')
    chain = MarkovChain(words)
    walk = chain.walk(20)
    print(walk)