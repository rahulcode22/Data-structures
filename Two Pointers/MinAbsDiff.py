'''
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1
'''
def minimize(a,b,c):
    i, j, k = 0, 0, 0
    diff = float('inf')
    res_i, res_j, res_k = 0, 0, 0
    while i <len(a) and j <len(b) and k < len(c):
        minimum = min(a[i],b[j],c[k])
        maximum = max(a[i],b[j],c[k])
        if maximum - minimum < diff:
            res_i = i
            res_j = j
            res_k = k
            diff = maximum - minimum
        if diff ==0:
            break
        if a[i] == minimum:
            i += 1
        elif b[j] == minimum:
            j += 1
        else:
            k += 1
    return diff

a = [1,4,5,8,10]
b = [6,9,15]
c = [2,3,6,6]
print minimize(a,b,c)
