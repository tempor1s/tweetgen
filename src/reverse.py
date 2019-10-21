from sys import argv


def reverse(s):
    # return ' '.join(reversed(s.split(' ')))
    str = ""
    for i in s:
        str = i + str
    return str


def reverse_word(s):
    return s[::-1]


def inplace_reverse(s):
    arr = s.split(' ')
    temp = []
    for s in arr:
        temp.append(s[::-1])
    return ' '.join(temp)


if __name__ == '__main__':
    args = ' '.join(argv[1:])
    print(reverse(args))
