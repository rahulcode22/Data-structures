#python program to print reverse of a string using stack
#Function to create an empty stack
def createstack():
    stack=[]
    return stack
#function to get the length of the stack
def length(stack):
    return len(stack)
#stack is empty if size is zero
def isempty(stack):
    return size(stack)==0
def push(item,stack):
    stack.append(item)
def pop(stack):
    return stack.pop()
#A stack based function to print reverse of string
def reverse(string):
    n=len(string)
    #create an empty stack
    stack=createstack()
    #pushing all characters of string to stack
    for i in range(n):
        push(stack,string[i])
    #make the string empty
    string=""
    #now pop all the characters from the string to string
    for i in range(n):
        string +=pop(stack)
    return string
#test above function
string="Python"
string =reverse(string)
print ("reversed string" +string)
