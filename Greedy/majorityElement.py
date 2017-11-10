'''
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
'''
import math
def majority(arr):
    n = len(arr)
    res = 0
    for i in arr:
        if arr.count(i) > math.floor(n/2):
            res = i
            break
    return res

print majority([2,1,2])
