'''
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.


'''
class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, num):

        num = str(num)
        if num == num[::-1]:
            return True
        else:
            return False
