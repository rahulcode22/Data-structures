#Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

#If there is no solution possible, return -1.

from sys import maxint
def maximumGap(arr):
    n = len(arr)
    start = 0
    end = n-1
    maximum = -maxint-1
    if n == 0 or n==1:
        return 0

    while (start < end):
        if arr[end] >= arr[start]:
            prev_max = end -start
            if maximum < prev_max:
                maximum = prev_max
            start +=1
        else:
            end -=1
    return maximum
