from itertools import permutations
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        return map(list, permutations(A))
