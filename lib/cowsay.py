from sys import argv

Cow = '''

   {}

   ^__^                             
   (oo)\_______                   
   (__)\       )\/\             
       ||----w |           
       ||     ||  
       
       '''


def cowsay(sentence):
    """
    Lets the cow say something!

    Params:
        sentence: str - The sentence that you want the cow to say

    Returns:
        The cow saying your sentence
    """
    sentence = ' '.join(sentence)
    return Cow.format(sentence)


if __name__ == '__main__':
    args = argv[1:]
    print(cowsay(args))
