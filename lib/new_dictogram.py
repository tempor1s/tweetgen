from histogram import histogram


class Dictogram(object):
    def __init__(self, dictogram):
        self.dictogram = dictogram
        self.sum = sum([self.dictogram.get(key, 0) for key in self.dictogram])

    
if __name__ == "__main__":
    histo = histogram('test.txt')
    dicto = Dictogram(histo)
    print(dicto.sum)