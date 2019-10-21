def reverse(s):
    return ' '.join(reversed(s.split(' ')))


def reverse_word(s):
    return s[::-1]


def inplace_reverse(s):
    arr = s.split(' ')
    temp = []
    for s in arr:
        temp.append(s[::-1])
    return ' '.join(temp)


if __name__ == '__main__':
    s = 'the walking dog'
    print(reverse_sentence(s))