from random import choice, randint

try:
    from lib.dictogram import Dictogram
    from lib.utils import get_clean_words
    from lib.queue import Queue
except ModuleNotFoundError:
    from queue import Queue
    from dictogram import Dictogram
    from utils import get_clean_words


class MarkovChain(dict):
    """MarkovChain is a markov chain implemented as a dict of histograms"""

    def __init__(self, word_list=None):
        """
        Initialize this markov as a new dict and set up inital markov chain

        Params:
            word_list: list - A list of the words you want to create a markov chain from
        """
        super().__init__()  # Initialize this as a new dict
        # Check to make sure a word list is passed in to do stuff, otherwise do nothing on init
        if word_list:
            self._create_chain(word_list)

    def _create_chain(self, word_list):
        n_words = len(word_list)
        for i, word in enumerate(word_list):
            if n_words > (i + 1):
                # The word 1 index ahead of the current word, aka the next word in the sentence
                next_word = word_list[i + 1]
            # The word dictogram if it exists
            word_dicto = self.get(word, None)
            # If word exists then add a count of 1, otherwise create a new dictogram with the next word
            if word in self:
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

        Returns:
            list: one random sampled word
        """
        histo = self.get(word, None)

        if histo:
            return histo.sample(1)
        else:
            raise KeyError('Invalid Word')

    def walk(self, count=10):
        """
        Walk through the markov states to get x amount of non-random words

        Params:
            count: int - The amount of times that you want it to walk

        Returns:
            list: x amount of random words
        """
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

    def create_sentence(self, count=10):
        """
        Create a sentence that is 'count' amount of words long

        Params:
            count: int - the length of the sentence

        Returns:
            str: the sentence that you requested
        """
        # Get count amount of words through markov walk
        words = self.walk(count)
        # Return a 'sentence' with a capital letter and a period at the end!
        return ' '.join(words).capitalize() + '.'


class HigherOrderMarkov(dict):
    def __init__(self, word_list=None, order=2):
        # TODO: use order
        self.order = order # the order of the markov chain
        if word_list:
            self.word_list = word_list # word list for later use
            self._create_chain(word_list) # create a chain
     
    def _create_chain(self, word_list):
        n_words = len(word_list)
        for i, key1 in enumerate(word_list):
            if n_words > (i + 2): # TODO: use order
                key2 = word_list[i + 1]
                word = word_list[i + 2]
                if (key1, key2) not in self:
                    self[(key1, key2)] = [word]
                else:
                    self[(key1, key2)].append(word)
    
    def walk(self, count=10):
        rand = randint(0, len(self.word_list))
        key = (self.word_list[rand], self.word_list[rand + 1])
        tweet = key[0] + ' ' + key[1]

        for _ in range(count):
            word = choice(self[key])
            tweet += ' ' + word
            key = (key[1], word)
        
        return tweet.capitalize() + '.'

if __name__ == "__main__":
    path = 'txt_files/donald.txt'
    words = get_clean_words(path)
    markov = HigherOrderMarkov(words)

    tweet = markov.walk(15)
    print(tweet)