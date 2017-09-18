class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def swap(self,x,y):
        if x is None or y is None:
            return
        if x == y:
            return
        #Kepping track of previous and current Node
        prevX = None
        currX= self.head

        prevY = None
        currY = self.head

        while (currX != None and currX.data != x):
            prevX = currX
            currX = currX.next
        while (currY != None and currY.data != y):
            prevY = currY
            currY = currY.next
        #if either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        #if x is not head of the LinkedList
        if prevX !=None:
            prevX.next = currY
        else:
            self.head = currY
        #if y is not the head of the LinkedList
        if prevY !=None:
            prevY.next = currX
        else:
            self.head = currX
        #swap the next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print temp.data
            temp =temp.next
#MAin program to test above function
ll =LinkedList()

ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
print "LinkedList before swapping "
ll.print_list()
print "LinkedList after swapping "
ll.swap(3,5)
ll.print_list()
