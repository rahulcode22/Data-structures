'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        i = 0
        j = len(A)-1
        while True:
            if i>j: break
            if not A[i].isalpha() and not A[i].isdigit():
                i+=1
                continue
            if not A[j].isalpha() and not A[j].isdigit():
                j-=1
                continue
            if not A[i].lower() == A[j].lower():
                return 0
            i+=1
            j-=1
        return 1
