'''

Given two binary strings, return their sum (also a binary string).
'''
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        a = int(A,2)
        b = int(B,2)
        c = bin(a+b)[2:]
        return c
