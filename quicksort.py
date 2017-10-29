from random import randint

count = 0

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

def partition(B, left, right):
    global count
    pivot = B[left]
    count += len(B) - 1
    i = left + 1
    for j in range(i,right):
        if B[j] < pivot:
            B[j], B[i] = B[i], B[j]
            i += 1
    B[left], B[i-1] = B[i-1], B[left]
    return B, i - 1

def choosePivot(C,n):
    pivot = randint(0, n - 1)
    first = 0
    last = n - 1
    mid = last / 2
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

from sys import argv

script, filename = argv

txt = open(filename)

file_list = [] 

for line in txt:
    file_list.append(int(line))

quickSort(file_list)
#print(quickSort(file_list))
print(count)