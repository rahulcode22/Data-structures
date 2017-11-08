'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3
'''
def singlenum(arr):
    res = 0
    for i in arr:
        res ^= i
    return res
arr= [1,2,2,3,1]
print singlenum(arr)
