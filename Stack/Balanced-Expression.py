class Stack:
    def __init__(self):
        self.items  = []

    #Push a new item to the last index
    def push(self,item):
        self.items.append(item)

    #Remove the last item
    def pop(self):
        #if stack is empty
        if  not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

def isBalanced(expression):
    s = Stack()
    balanced = True
    index = 0
    while index < len(expression) and balanced:
        symbol = expression[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print isBalanced('(())')
