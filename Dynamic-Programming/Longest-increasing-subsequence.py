"""find the length of the longest subsequence of a given sequence
such that all elements of the subsequence are sorted in increasing order.
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6
and LIS is {10, 22, 33, 50, 60, 80}"""
#Dynamic Programming Approach
#Complexity O(n^2)
#There is better way to do this in O(nlogn) but to show u a simple example of DP
#We have used thi LCS example
def lis(arr):
    n = len(arr)

    lis = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] and lis[i] < lis[j]+1:
                lis[i] = lis[j] + 1

    maximum = 0
    return max(lis)

arr = [10,22,9,33,21,50,41,60]
print lis(arr)
