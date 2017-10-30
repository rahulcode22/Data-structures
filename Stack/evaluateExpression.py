'''Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

'''
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                # here take care of the case like "1/-22",
                # in Python 2.x, it returns -1, while in
                # Leetcode it should return 0
                    if l*r < 0 and l % r != 0:
                        stack.append(l/r+1)
                    else:
                        stack.append(l/r)
        return stack.pop()
