#Find the contiguous subarray within an array 
#(containing at least one number) which has the largest sum.
from sys import maxint
    def maxSubArray(self, a):
        max_so_far = -maxint - 1
        max_ending_here = 0

        for i in range(0, len(a)):
            max_ending_here = max_ending_here + a[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
