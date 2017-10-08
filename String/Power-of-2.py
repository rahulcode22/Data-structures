'''
Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.
'''
class Solution:
    # @param A : string
    # @return an integer
    def power(self, num):
        num = int(num)
        if num == 1:
            return 0
        while num != 1:
            if num%2 != 0:
                return 0
            num = num/2
        return 1
