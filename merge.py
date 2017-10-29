def msort(list1):
    result = []
    if len(list1) < 2:
        return list1
    mid = int(len(list1)/2)
    left = msort(list1[:mid])
    right = msort(list1[mid:])
    inv = 0
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.pop(0)
                inv += 1
            else:
                result.append(left[0])
                left.pop(0)
        elif len(right) > 0:
            for i in right:
                result.append(i)
                right.pop(0)
        else:
            for i in left:
                result.append(i)
                left.pop(0)
                inv += 1
    return result
"""
def merge(list2):
    inv = 0
    inv += msort(list2)
    return inv

list_new = [1,56,34,23,67,12,78,34]

print(msort(list_new))
#print(merge(list_new))
"""