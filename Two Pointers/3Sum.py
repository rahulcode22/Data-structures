'''

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''
def closestSum(arr,target):
    i = 0
    arr = sorted(arr)
    min_ = float('inf')
    n = len(arr)
    res= 0
    while (i < n):
        j = i+1
        k = n-1
        while (j<k):
            sum_ = arr[i]+arr[j]+arr[k]
            diff = abs(sum_ - target)
            if diff == 0:
                return sum_
            if diff < min_:
                min_ = diff
                res = sum_
            if sum_ <= target:
                j += 1
            else:
                k -= 1
        i += 1
    return res

arr = [-1,2,1,-4]
target = 1
print closestSum(arr,target)
