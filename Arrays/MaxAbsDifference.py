#You are given an array of N integers, A1, A2 ,…, AN.
#Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
#f(i, j) is defined as |A[i] - A[j]| + |i - j|,
#where |x| denotes absolute value of x.
#For ex-
#A=[1, 3, -1]

#f(1, 1) = f(2, 2) = f(3, 3) = 0
#f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
#f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
#f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

#So, we return 5.
from sys import maxint
def maxArr(arr):

        max1 = -maxint -1
        max2 = -maxint -1
        max3 = -maxint -1
        max4 = -maxint -1
        ans = -maxint -1

        for i in range(0,len(arr)):
            max1 = max(max1,arr[i]+i)
            max2 = max(max2,-arr[i]+i)
            max3 = max(max3,arr[i]-i)
            max4 = max(max4,-arr[i]-i)

            min1 = min(min1,A[i] + i)
            min2 = min(min2,A[i] - i)
            min3 = min(min3,-A[i]+i)
            min4 = min(min4,-A[i]-i)

        ans = max(ans,max1-arr[i]-i)
        ans = max(ans,max2+arr[i]-i)
        ans = max(ans,max3-arr[i]+i)
        ans = max(ans,max4+arr[i]+i)
        return ans
