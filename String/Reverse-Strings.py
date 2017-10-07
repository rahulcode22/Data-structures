'''Given an input string, reverse the string word by word.'''
class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, a):

        s = a.split()
        s.reverse()
        res = " ".join(s)
        return res
