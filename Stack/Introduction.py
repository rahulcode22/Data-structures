'''-->It is a linear data structure.
-->Follows a paarticular order in which the operations are performed.'
-->Order may be FILO or LIFO
-->Main operations are
  1)push-->Add an item in the stack
  2)pop-->removes an item in the stack
  3)peek-->get the topmost item.
 -->stack may be implemented using two ways:
        1)using linked list
        2)using arrays
        '''
from sys import maxsize
#fucntion to create Stack
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)
    print "pushed to stack" + item

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()

stack = createStack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
push(stack,str(40))
print pop(stack) + "Popped from stack"






#Implementing stack using linkedList
class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True is self.root is None else False

    def push(self,data):
        new_node = StackNode(data)
        new_node.next = self.root
        self.root = new_node

    def pop(self):
        if self.isempty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        Popped = temp.data
        return Popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data

#Driver program to test above class
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print "%d popped from stack" %(stack.pop())

print "Top element is %d" % (stack.peek())
