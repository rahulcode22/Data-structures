#import maxsize from sys.Maxsize returns infinite when stack is empty.
from sys import maxsize
#function to create a stack.initial size of stack is zero
def createstack():
    stack=[]
    return stack
if isempty(stack):
    return len(stack)==0
    
#push function to add an item on the stack.Increases stack size by 1
def push(stack,item):
    stack.append(item)
    print ("item pushed"+item)
#pop function to remove item from stack.Decreases stack size by 1.
def pop(stack):
    if (isempty(stack)):
        return str(-maxsize-1)
    stack.pop()
#peek function.return top element of the stack
def peek(stack):
    if (isempty(stack)):
        return str(-maxsize-1)
    return stack[-len(stack)-1]
#driver program to test the above functions
satack=createstack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
push(stack,str(40))
print(pop(stack) +" is popped from stack")
print("top item is "+peek(stack))




    
