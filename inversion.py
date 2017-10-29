from sys import argv

script, filename = argv

txt = open(filename)

file_list = []

for line in txt:
    file_list.append(int(line))

def sortCount(A):
    mid = int(len(A)/2)
    if len(A) < 2:
        return A, 0 
    X = A[:mid]
    Y = A[mid:]
    X, x = sortCount(X)
    Y, y = sortCount(Y)
    Z, z = mergeCount(X,Y)
    return Z, x + y + z

def mergeCount(X, Y):
    R = []
    inv = 0
    while X and Y:
        if X[0] > Y[0]:
            R.append(Y[0])
            Y.pop(0)
            inv += len(X)
        else:
            R.append(X[0])
            X.pop(0)
    R += X + Y
    return R, inv

#print(file_list)

print(sortCount(file_list))