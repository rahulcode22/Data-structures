'''
Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, arr):

        n = len(arr)
        ans = 0
        for i in range(32):
            count = 0
            for j in range(n):
                if (arr[j] & (1 << i)):
                    count +=1
            ans += (count*(n-count)*2)
        return ans%1000000007
