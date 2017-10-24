'''You want to be able to access the largest element in a stack.''''
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

class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self,item):
        self.stack.push(item)
        if self.max_stack.peek() is None or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.max_stack.peek():
            self.max_stack.pop()
        return item

    def get_max(self):
        return self.max_stack.peek()
