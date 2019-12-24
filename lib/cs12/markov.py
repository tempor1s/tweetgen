from random import choice, randint, seed
from collections import defaultdict, deque
import re

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
        self.order = order  # the order of the markov chain
        if word_list:
            self.word_list = word_list  # word list for later use
            self._create_chain(word_list)  # create a chain

    def _create_chain(self, word_list):
        n_words = len(word_list)
        for i, key1 in enumerate(word_list):
            if n_words > (i + self.order):
                key2 = word_list[i + 1]
                word = word_list[i + 2]
                words = []

                for j in range(self.order):
                    words.append(word_list[i + j])

                entry = tuple(words)

                if entry not in self:
                    self[entry] = [word]
                else:
                    self[entry].append(word)

    def walk(self, count=10):
        rand = randint(0, len(self.word_list))
        key = (self.word_list[rand], self.word_list[rand + 1])
        tweet = key[0] + ' ' + key[1]

        for _ in range(count):
            word = choice(self[key])
            tweet += ' ' + word
            key = (key[1], word)

        return tweet.capitalize() + '.'

class ImprovedMarkovChain(dict):
    def __init__(self, corpus=[], order=2):
        self.init_memory = Queue(order)
        self.memory = Queue(order)
        
        for word in corpus + corpus[:order]:
            self.add_state(word)
        
    def add_state(self, new_state):
        current_state = self.init_memory.serialize()

        if current_state in self:
            self[current_state].append(new_state)
        else:
            self[current_state] = [new_state]
        
        self.init_memory.enqueue(new_state)
    
    def sample(self, N=1, starting_state=tuple()):
        for state in starting_state:
            self.memory.enqueue(state)
        
        for _ in range(N):
            next_state = choice(self[starting_state])
            self.memory.enqueue(next_state)
            yield next_state
            starting_state = self.memory.serialize()
        self.memory.clear()


class BigBrainMarkovChain(Dictogram):
    def __init__(self, n=1):
        super().__init__()  
        self.n = n
        
    def build_state_histogram(self, words_list):
        tokens = Queue(words_list[0:self.n])
        for index in range(self.n-1, len(words_list)):
            if tokens not in self:
                self[tuple(tokens)] = Dictogram()
            try:
                self[tuple(tokens)].add_count(words_list[index + 1])
                tokens.enqueue(words_list[index + 1])
            except:
                self[tuple(tokens)] = Dictogram(['**STOP**'])
            tokens.dequeue()

    def get_next_word(self, tokens):
        return self[tokens].sample()

    def build_sentence(self, num_words, words_list):
        self.build_state_histogram(words_list)
        sentence = []
        first_words = choice(list(self.keys()))
        tokens = Queue(self.n)
        for word in first_words:
            tokens.enqueue(word)
        sentence.extend(first_words)
        total_words = len(first_words)

        while total_words < num_words:
            next_word = self.get_next_word(tuple(tokens.items()))
            if next_word == '**STOP**':
                sentence.append(next_word)
                break
            sentence.append(next_word)
            tokens.dequeue()
            tokens.enqueue(next_word)
            total_words += 1
        return ' '.join(sentence)


class NarkovChain(dict):
    # Audi :)
    # convert this to use the states as tuples
    def __init__(self, word_list, order=2):
        super().__init__()
        # the order the markov chain will be using
        self.order = order

        # create the markov chain
        if word_list is not None:
            self['start'] = Dictogram()
            self.create_chain(word_list)
        # empty variable for the sentence
        self.sentence = None
    
    def create_chain(self, word_list):
        start = 0 # point to start slicing
        end = self.order # point to end slicing - slice excludes the end point[]

        while end <= len(word_list):
            # take a slice
            state = ' '.join(word_list[start:end])

            # check if the state is in the histogram already
            if self.get(state) == None:
                # not in histogram so add it
                self[state] = Dictogram()

            # check if token should go in start state
            # checks for capitalization
            if re.match('[A-Z]', state) is not None:
                self.get('start').add_count(state)
            
            # increment state
            start += 1
            end += 1

            # bounds check
            if end <= len(word_list):
                # look at next state
                next_state = ' '.join(word_list[end-1:end])
                # add next state to current state
                self.get(state).add_count(next_state)
    
    def generate_sentence(self):
        # choose a random word from start dictogram
        sentence_list = []
        sentence_list.extend(self['start'].sample())

        stop_token_hit = False

        # loop until we hit a stop token
        while stop_token_hit is False:
            # look at current sentence
            end = len(sentence_list)
            # take n last words
            state = ' '.join(sentence_list[end - self.order:end])
            # sample the state and add it to a list
            if self.get(state) is None:
                sentence_list.append('.')
                stop_token_hit = True
            else:
                sampled_word = self.get(state).sample()[0]

                if re.search('[$\.\?\!]', sampled_word) is not None:
                    stop_token_hit = True
                
                sentence_list.append(sampled_word)
            
        return ' '.join(sentence_list)

class DavidMarkov(object):
    """A class for generating markov chains and walking through them"""

    def __init__(self, word_file):
        """Initilize starting variables"""
        self.word_list = read_file_words(word_file)
        self.markov = self.make_chain(self.word_list)

    def make_chain(self, word_list):
        """Create and return a markov chain from a list of words"""
        markov = {}
        for i in range(len(word_list)):
            if word_list[i] not in markov:
                markov[word_list[i]] = []
            if i < len(word_list) - 1:
                markov[word_list[i]].append(word_list[i + 1])

        for key in markov:
            markov[key] = Dictogram(markov[key])

        return markov

    def walk(self, length):
        """Randomly walk down a markov chain to generate a sentence"""
        output = []
        output.append(choice(tuple(self.markov.keys())))
        for i in range(length):
            output.append(self.markov[output[i]].sample())

        string = ""
        for word in output:
            string += word + " "

        return string


class DavidMarkovN(DavidMarkov):
    """A Markov chain of the nth order"""

    def __init__(self, word_file, n):
        """Initialize starting values"""
        self.n = n
        self.word_list = get_clean_words(word_file)
        self.markov = self.make_chain(self.word_list)

    def make_chain(self, word_list):
        """Create and return a markov chain from a given list of words"""
        markov = {}
        q = Queue()
        for i in range(len(word_list)):
            if i < self.n:
                q.enqueue(word_list[i])
            else:
                key = str(q)
                q.dequeue()
                q.enqueue(word_list[i])
                if markov.get(key) is None:
                    markov[key] = []
                markov[key].append(str(q))

        for key in markov:
            markov[key] = Dictogram(markov[key])

        return markov

    # @time_it
    def walk(self, length=0, ends=0):
        """Randomly walk down a markov chain to generate a sentence"""
        output = []
        output.append(choice(tuple(self.markov.keys())))

        # Start token should be a start token
        while output[0].find("[S]") != 0:
            output[0] = choice(tuple(self.markov.keys()))

        output[0] = output[0]
        # Tracking end tokens
        tokens = 0
        i = 0
        while tokens < ends:  # or i < length:
            try:
                next_set = self.markov[output[i]].sample()
                last = next_set[len(next_set) - 3:len(next_set)]
                if last == "[E]":
                    tokens += 1
                output.append(next_set)
                i += 1
            except KeyError:
                break

        string = ""
        for word in output:
            if output.index(word) == 0:
                string += word.replace("[S]", "").replace("[E]", "") + " "
            else:
                try:
                    text = word.split()[-1].replace("[S]", "")
                    string += text.replace("[E]", "") + " "
                except KeyError:
                    return string

        return string

# class ImprovedMarkovChain(object):
#     def __init__(self, order=2):
#         self.order = order
#         self.lookup_dict = defaultdict(list)
#         self.punctuation_regex = re.compile('[/,.!;\?\:\-\[\]\(\)\"\\\n]+')
#         self._seeded = False
#         self._gen_seed()

#     def _gen_seed(self, rand_seed=None):
#         if self._seeded != True:
#             try:
#                 if rand_seed is not None:
#                     seed(rand_seed)
#                 else:
#                     seed()
#                 self._seeded = True
#             except NotImplementedError:
#                 self._seeded = False

#     def add_file(self, file_path):
#         content = ''
#         with open(file_path, 'r') as f:
#             self._add_source_data(f.read())

#     def add_string(self, string):
#         self._add_source_data(string)

#     def _add_source_data(self, string):
#         clean_str = self.punctuation_regex.sub(' ', string).lower()
#         tuple_keys = self._generate_tuple_keys(clean_str.split())
#         for t in tuple_keys:
#             self.lookup_dict[t[0]].append(t[1])

#     def _generate_tuple_keys(self, data):
#         if len(data) < self.order:
#             return

#         for i in range(len(data) - self.order):
#             yield [tuple(data[i:i+self.order]), data[i+self.order]]

#     def generate_text(self, max_length=20):
#         context = deque()
#         output = []

#         if len(self.lookup_dict) > 0:
#             self._gen_seed(rand_seed=len(self.lookup_dict))

#             idx = randint(0, len(self.lookup_dict) - 1)
#             chain_head = list(self.lookup_dict.keys())[idx]
#             context.extend(chain_head)

#             while len(output) < (max_length - self.order):
#                 next_choices = self.lookup_dict[tuple(context)]
#                 if len(next_choices) > 0:
#                     next_word = choice(next_choices)
#                     context.append(next_word)
#                     output.append(context.popleft())
#                 else:
#                     break
#             output.extend(list(context))

#         return output


if __name__ == "__main__":
    words = get_clean_words('txt_files/example.txt')

    markov = ImprovedMarkovChain(words, 2)
    print(markov)

    print(' '.join(markov.sample(10)))