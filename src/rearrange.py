from sys import argv
from random import shuffle, randint
from utils import time_it

@time_it
def rearrange(arr):
    # Fisher Yates Implementation
    # Create a copy so that we are not modifiying the passed in array - slower but safe
    new_arr = list(arr)
    # Loop through the length of the array
    for i in range(len(new_arr)):
        # Chose a random value between 0 and int
        j = randint(0, i)
        
        # Swap new_arr[i] with the element at random index using fancy python things reassignment :)
        new_arr[i], new_arr[j] = new_arr[j], new_arr[i]

    return new_arr


def fisher_yates_shuffle(the_list):
    amnt_to_shuffle = len(the_list)
    while amnt_to_shuffle > 1:
        i = int(floor(random() * amnt_to_shuffle))
        amnt_to_shuffle -= 1
        the_list[i], the_list[amnt_to_shuffle] = the_list[amnt_to_shuffle], the_list[i]
    return the_list


def lazy_rearrange(arr):
    new_arr = list(arr)
    shuffle(new_arr)
    return ' '.join(new_arr)


if __name__ == '__main__':
    # Trying to be verbose, could 1 line this :P
    args = argv[1:]
    rearranged = rearrange(args)
    print(rearranged)