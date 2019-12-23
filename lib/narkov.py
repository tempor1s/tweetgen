import random
import re

try:
    from lib.dictogram import Dictogram
    from lib.utils import get_clean_words
    from lib.queue import Queue
except ModuleNotFoundError:
    from queue import Queue
    from dictogram import Dictogram
    from utils import get_clean_words


class Narkov(dict):
    def __init__(self, word_list, order=2):
        super().__init__()
        self.order = order  # order of the markov chain
        self.memory = Queue(order)  # for sampling from markov model
        self.init_memory = Queue(order)  # for building the markov model

        if word_list is not None:
            # self['**START**'] = Dictogram()
            # self['**END**'] = Dictogram()
            self._create_chain(word_list)

    def _create_chain(self, word_list):
        for i, message in enumerate(word_list):
            if i < self.order: # to fill the queue initally so that we do not add states that are smaller than order
                self.init_memory.enqueue(message) # enqueue each new item
            else:
                current_state = self.init_memory.serialize() # the current state
                self.init_memory.enqueue(message) # create the new state
                new_state = self.init_memory.serialize() # the next state

                if current_state in self: # check to see if the state already exists
                    self[current_state].add_count(new_state) # if it does just add the next state to it
                else:
                    self[current_state] = Dictogram([new_state]) # otherwise create a new dictogram with the new state
    
    def generate_sentence(self, length=10, starting_state=()):
        # start = self['**START**'].sample(1)[0] # word from starting state
        # sentence = [].extend(start) # the start of the sentence :)
        
        # while True:
        #     pass
        starting_state = random.choice(list(self.keys()))
        print(starting_state)

        for _ in range(length):
            next_state = self[starting_state].sample()[0]
            print(next_state)
            self.memory.enqueue(next_state)
            yield next_state
            starting_state = self.memory.serialize()
        self.memory.clear()

                

if __name__ == "__main__":
    words = get_clean_words('txt_files/example.txt')

    m = Narkov(words, 3)

    print(' '.join(m.generate_sentence()))
