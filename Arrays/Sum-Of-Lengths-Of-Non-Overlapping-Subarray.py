#Given an array of N elements, you are required to
#find the maximum sum of lengths of all non-overlapping subarrays
# with K as the maximum element in the subarray.

#Complexity  O(n)

def LongestSubsequence(arr,n,k):
    lis =[]
    curr_len = 0
    max_len  = 0
    for i in range(n):
        if arr[i] <= k:
            lis.append(arr[i])
            curr_len +=1
        else:
            if k in lis:
                max_len += curr_len
                curr_len  = 0
                lis = []

            else:
                lis = []
                curr_len = 0
    if k in lis:
        max_len +=curr_len
        curr_len = 0
        lis = []

    else:
        lis = []

        curr_len = 0
    return max_len

arr = [4, 5, 7, 1, 2, 9, 8, 4, 3, 1]
n = len(arr)

print LongestSubsequence(arr,n,4)
