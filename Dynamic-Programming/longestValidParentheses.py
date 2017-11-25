'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''
class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, string):
        n = len(string)
        stack = [-1]
        res = 0
        for i in range(n):
            if string[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    res = max(res, i- stack[len(stack)-1])
                else:
                    stack.append(i)
        return res
