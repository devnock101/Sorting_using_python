from sys import argv
from collections import Counter

script, filename = argv

g = {}

with open(filename) as txt:
    for line in txt:
        ints = [int(x) for x in line.split()]
        g[ints[0]] = Counter(ints[1:])

print(g)