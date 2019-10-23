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
    sentence = ' '.join(sentence)
    return Cow.format(sentence)


if __name__ == '__main__':
    args = argv[1:]
    print(cowsay(args))