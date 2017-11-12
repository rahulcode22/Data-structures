class Solution:
    def __init__(self):
        self.phone_map = {
            '0': ['0'],
            '1': ['1'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        if len(A) == 0:
            return []

        if A in self.phone_map:
            return self.phone_map[A]
        n = len(A)
        left_combos = self.letterCombinations(A[:n/2])
        right_combos = self.letterCombinations(A[n/2:])
        possible_combos = [left + right for left in left_combos for right in right_combos]
        self.phone_map[A] = possible_combos
        return possible_combos
