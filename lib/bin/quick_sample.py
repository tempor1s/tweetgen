import bisect
import random
from collections import Counter, Sequence

def weighted_sample(population, weights, k):
    return random.sample(WeightedPopulation(population, weights), k)

# https://stackoverflow.com/questions/13047806/weighted-random-sample-in-python#comment17723531_13048274 - credit
class WeightedPopulation(Sequence):
    def __init__(self, population, weights):
        assert len(population) == len(weights) > 0
        self.population = population
        self.cumweights = []
        cumsum = 0 # compute cumulative weight
        for w in weights:
            cumsum += w   
            self.cumweights.append(cumsum)  
    def __len__(self):
        return self.cumweights[-1]
    def __getitem__(self, i):
        if not 0 <= i < len(self):
            raise IndexError(i)
        return self.population[bisect.bisect(self.cumweights, i)]


total = Counter()
for _ in range(1000):
    sample = weighted_sample("abc", [1,10,2], 5)
    total.update(sample)
print(sample)
print("Frequences %s" % (dict(Counter(sample)),))

# Check that values are sane
print("Total " + ', '.join("%s: %.0f" % (val, count * 1.0 / min(total.values()))
                           for val, count in total.most_common()))