#from random import randint
from merge import msort

#count = 0

"""
def quickSort(A):
    n = len(A)
    if n < 2:
        return A
    pivot = choosePivot(A,n)
    A[0], A[pivot] = A[pivot], A[0]
    A, pivot = partition(A, 0, n)
    X = quickSort(A[:pivot])
    Y = quickSort(A[pivot + 1:])
    X.append(A[pivot])
    return  X + Y

def rselect(A, i):
    n = len(A)
    if n < 2:
        return A[0]
    pivot = choosePivot(A,n)
    A[0], A[pivot] = A[pivot], A[0]
    A, pivot = partition(A, 0, n)
    j = pivot + 1
    if j == i:
        return A[pivot]
    elif j > i:
        return rselect(A[:pivot], i)
    elif j < i:
        return rselect(A[pivot + 1:], i - pivot)
"""

def dselect(A, i):
    n = len(A)
    if n < 2:
        return A[0]
    pivot = choosePivot(A,n)
    j = A.index(pivot)
    A[0], A[j] = A[j], A[0]
    A, j = partition(A, 0, n)
    if j + 1 == i:
        return A[j]
    elif j + 1 > i:
        return dselect(A[:j], i)
    elif j + 1 < i:
        return dselect(A[j + 1:], i - j)

def partition(B, left, right):
    global count
    pivot = B[left]
    #count += len(B) - 1
    i = left + 1
    for j in range(i,right):
        if B[j] < pivot:
            B[j], B[i] = B[i], B[j]
            i += 1
    B[left], B[i-1] = B[i-1], B[left]
    return B, i - 1

def choosePivot(C,n):
    n1 = n/5
    if n1 < 2:
        return C[(n1 - 1) / 2]
    D = []
    for x in range(0,n,5):
        Y = msort(C[x : x + 5])
        D.append(Y[2])
    return choosePivot(D, n / 10)

"""
def choosePivot(C,n):
    pivot = randint(0, n - 1)
    first = 0
    last = n - 1
    mid = last / 2
    #return pivot
    return med(C, first, last, mid)

def med(D,a,b,c):
    if D[a] > D[b]:
        if D[b] > D[c]:
            return b
        elif D[c] > D[a]:
            return a
        else:
            return c
    else:
        if D[b] < D[c]:
            return b
        elif D[c] < D[a]:
            return a
        else:
            return c
"""

list_new = [6546,654654,84848,565,54,658964,1515,65654,61351,9879598]

#list_len = len(list_new)

find = 8

print(msort(list_new))
print(dselect(list_new, find))

'''
from sys import argv

script, filename = argv

txt = open(filename)

file_list = [] 

for line in txt:
    file_list.append(int(line))

quickSort(file_list)
print(count)
'''