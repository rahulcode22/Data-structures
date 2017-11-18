def lbs(arr):
    n = len(arr)
    lis = [1 for i in range(n+1)]

    for i in range(1,n):
        for j in range(0, i):
            if (arr[i] > arr[j]) and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
    lds = [1 for i in range(n+1)]

    for i in reversed(range(n-1)):#loop from n-2 to 0
        for j in reversed(range(i-1,n)):#loop from n-1 downto i-1
            if arr[i] > arr[j] and lds[i] < lds[j]+1:
                lds[i] = lds[j]+1

    maximum = lis[0] + lds[0] - 1
    for i in range(1, n):
        maximum = max((lis[i]+lds[i]-1),maximum)
    return maximum

arr =  [ 64, 263, 11, 188, 396, 268, 116, 453, 207, 39, 312, 401, 396, 476, 56, 277, 104, 213, 79, 128, 36, 393, 117, 298, 371, 73, 110, -3, 350, 144, 210, 491, 312, 351, 183, 25, 230, 303, 478, 476, 276, 127, 184, 390, 481, 63, 270, 417, 257, 189, 18, 53, 80, 122, 358, 469, 244, 144, 152, 83, 188, 174, 381, 499, 280, 67, -1, 95, 489, 428, 302, 327, 25, 419, 207, 499, 457, 239, 12, 438, 54, 473, 116, 355, 428, -8, 37, 292, 116, 361, 186, 396, 375, -8, 416, 21, -8, 231, 51, 271, 318, 214, 361, 196, 118, 434, 133, 366, 192, 244, 400, 88, 444, 251, 165, 286, 15, 0, 223, 74, 84, 456, 464, 50, 209, 137, 67, 74, 4, 397, 403, 156, 70, 39, 187, 483, 267, 187, 464, 361, 74, 398, 479, 107, 123, 358, 317, 209, 192, 157, 61, 437, 330, -2, 276, 418, 418, 286, 303, 335, 317, 394, 193, 252, 64, 71, 322, 397, 494, 480, 285, 25, 298, 227, 16, 382, 452, 75, 304, 172, 469, 334, 294, 181, 394, 163, 326, 169, 30, 39, 425, 105, 294, 354, 207, 314, 386, 494 ]
print "Length of LBS is",lbs(arr)

#Another Approach
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        m=0
        L=[1]*len(A)
        for i in range(1,len(A)):
            for j in range(i):
                if A[j]<A[i]:
                    L[i]=max(L[i],L[j]+1)
        R=[1]*len(A)
        for i in range(len(A)-2,-1,-1):
            for j in range(len(A)-1,i,-1):
                if A[j]<A[i]:
                    R[i]=max(R[i],R[j]+1)
        for i in range(len(A)):
            val=L[i]+R[i]-1
            if val>m:
                m=val
        return m
