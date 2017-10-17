'''
You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:

You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

Return answer modulo 109 + 7.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, arr):
        arr = sorted(arr)
        count = 0
        n = len(arr)
        if len(arr) < 3:
            return 0
        for i in range(0,n-2):
            k = i+2
            for j in range(i+1,n):
                while (k < n and arr[i] + arr[j] > arr[k]):
                    k += 1
                count += k - j - 1
        return count%(10**9 + 7)
