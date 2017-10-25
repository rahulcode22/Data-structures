'''
1.Create an empty stack called 'opstack' for keeping operators.Create an empty list for output.
2.Convert the input infix string to a list using split method.
3.Scan the token list from left to right.
    ->If the token is an operand,apppend it to the end of output list.
    ->If token is a left parenthesis, push it on the stack
    ->If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed.Append each operator to the end of the output list.
    ->If the token is an operator, *,/,+ or -, push it on the opstack.However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
4.When the input expression has been completely processed, check the opstack.Any operators still on the stack can be removed and appended to the end of the output list.
'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

def infixToPostfix(expr):
    precedence = {}
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["("] = 1
    opstack = Stack()
    postfixList = []
    tokenList = expr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            while (not opstack.isEmpty()) and precedence[opstack.peek()] >= precedence[token]:
                postfixList.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())
    return " ".join(postfixList)

print infixToPostfix("A * B + C * D")
