'''
Write a program to validate if the input string has redundant braces?
Return 0/1

0 -> NO
1 -> YES
'''
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for el in A:
            if el == "(":
                stack.append(el)
            elif el == "+" or el == "-" or el == "/" or el == "*":
                stack.append("exp")
            elif el == ")":
                if stack[-1] == "exp":
                    stack.pop()
                    stack.pop()
                else:
                    return 1
        else:
            return 0
