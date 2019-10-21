from random import choice

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")


def random_python_quote():
    return choice(quotes)


if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)