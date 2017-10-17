'''
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.
'''
def intersection(a,b):
    i =0
    j = 0
    lis = []
    if a == b:
        return a
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        elif a[i] == b[j]:
            lis.append(a[i])
            i +=1
            j += 1
    return lis

a = [1,2,3,3,4,5,6]
b = [3,3,5]
print intersection(a,b)
