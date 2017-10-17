'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
'''
def check(arr):
    i = 0
    arr =  sorted(arr)
    n = len(arr)
    lis = []
    while i < n:
        j = i + 1
        k = n - 1
        while j < k:
            sum_ = arr[i] + arr[j] + arr[k]
            if sum_ == 0:
                lis.append((arr[i],arr[j],arr[k]))
            if sum_ <= 0:
                j += 1
            else:
                k -= 1
        i += 1
    lis = list(set(lis))
    return lis
arr = [-1,0,1,2,-1,-4]
print check(arr)
