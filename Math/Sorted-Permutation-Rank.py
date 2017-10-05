'''
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

EXAMPLE:
Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' :
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
'''
from itertools import permutations
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, st):

        def fact(n):

            f = 1
            while n >= 1:
                f = f*n
                n = n-1
            return f

        def findSmallerInRight(st,low,high):
            countRight = 0
            i = low + 1
            while i <= high:
                if st[i] < st[low]:
                    countRight += 1
                i = i + 1
            return countRight

        mul = fact(len(st))
        rank = 1
        i = 0
        while i < len(st):
            mul = mul/(len(st)-i)
            #count no of chars smaller than str[i] from str[i+1] to str[len-1]
            countRight = findSmallerInRight(st,i,len(st)-1)
            rank = rank + countRight*mul
            i = i+1
        for i in set(st):
            if st.count(i) > 1:
                rank =rank/fact(st.count(i))
                
        return rank%1000003
