'''
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.
'''
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, a, b):
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
