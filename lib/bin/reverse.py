from sys import argv


def reverse(s):
    """
    Reverse a string

    Params:
        s: str - The string you want to reverse

    Returns:
        str: The reversed string
    """
    str = ""
    for i in s:
        str = i + str
    return str


def reverse_word(s):
    """
    Reverse a word

    Params:
        s: str - The word to reverse

    Returns:
        str: The reversed string
    """
    return s[::-1]


def inplace_reverse(s):
    """
    Reverse each word in a string without changing the order

    Params:
        s: str - The string you want to reverse

    Returns:
        str: The reversed string
    """
    arr = s.split(' ')
    temp = []
    for s in arr:
        temp.append(s[::-1])
    return ' '.join(temp)


if __name__ == '__main__':
    args = ' '.join(argv[1:])
    print(reverse(args))
