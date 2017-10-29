from sys import argv
from random import choice
'''
script, filename = argv

#filename = "C:\Users\crude\Documents\random.txt"

txt = open(filename)

mygraph = {}

"""
line = txt.readline()
line = txt.readline()
line1 = line.split("\t")
print(line)
line_list = list(map(int,line1[:-1]))
myset = set(line_list[1:])
key = line_list[0]
mygraph[key] = myset
"""

for line in txt:
    line1 = line.split("\t")
    line_list = list(map(int,line1[:-1]))
    myset = set(line_list[1:])
    key = line_list[0]
    mygraph[key] = myset

txt.close()
'''
def rand_contract(A):
    while len(A) > 1:
        u = choice(list(A.keys()))
 
        edge_with_u = set(A.keys()) & A[u][0]
        edge_with_u.discard(u)

        v = choice(list(edge_with_u))
      
        if set([u]).issubset(A[v][0]):
            A[v][0].discard(u)
            A[v][2] += 1
            A[v][1] -= A[v][2]
#            A[v][1] += A[v][2]
 #           A[v][1] -= 1
  #          A[v][2] += 1

        if set([v]).issubset(A[u][0]):
            A[u][0].discard(v)
            A[u][2] += 1
            A[u][1] -= A[u][2]
            #A[u][1] += A[u][2]
            #A[u][1] -= 1
            #A[u][2] += 1

        p = A.pop(u)
        q = A.pop(v)
        r = p[0] | q[0]
        s = p[1] + q[1]
        t = p[2] + q[2]

        A[u] = [r,s,t]

        for i in list(A.keys()):
            if set([v]).issubset(A[i][0]):
                A[i][0].discard(v)
                A[i][0].add(u)

    min_cut = A
    return min_cut

graph = {1: [set([2,3,4]),3,0], 2: [set([1,3,4]),3,0], 3: [set([1,2,4,5]),4,0], 4: [set([1,2,3,6]),4,0], 5: [set([3,6,7,8]),4,0], 6: [set([4,5,7,8]),4,0], 7: [set([5,6,8]),3,0], 8: [set([5,6,7]),3,0]}

print(rand_contract(graph))
"""
#print(mygraph)
print(rand_contract(mygraph))
"""