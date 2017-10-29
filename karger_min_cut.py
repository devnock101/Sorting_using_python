from random import choice
from collections import Counter
from copy import deepcopy
from sys import argv

script, filename = argv

g = {}

with open(filename) as txt:
    for line in txt:
        ints = [int(x) for x in line.split()]
        g[ints[0]] = Counter(ints[1:])

def kargerMinCut(g):
    while len(g) > 2:
        #Selecting a random vertex
        u = choice(g.keys())
        #Edges and their number, starting from the first vertex
        gu = g[u]
        #Selecting the vertex with the maximum number of edges with the first vertex
        v = gu.most_common(1)[0][0]
        #Edges and their number, starting from the second vertex
        gv = g[v]
        #Deleting the second vertex from the graph
        del g[v]
        #Deleting self-loop
        del gv[u]
        del gu[v]
        #Merging second vertex into first vertex
        gu.update(gv)
        for w in gv:
            gw = g[w]
            gw[u] += gw[v]
            del gw[v]
    return g.itervalues().next().most_common(1)[0][1]

cuts = [kargerMinCut(deepcopy(g)) for x in range(5)]
'''
graph = {1:Counter([2,3,4]),
         2:Counter([1,3,4]),
         3:Counter([1,2,4,5]),
         4:Counter([1,2,3,6]),
         5:Counter([3,6,7,8]),
         6:Counter([4,5,7,8]),
         7:Counter([5,6,8]),
         8:Counter([5,6,7])
         }

cuts = [kargerMinCut(deepcopy(graph)) for x in range(5)]
'''
print(min(cuts), cuts)