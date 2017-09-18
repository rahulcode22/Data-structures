class Node:
    """Fucntion to intialize the Node object"""
    def __init__(self,data):
        self.data = data #Assign data
        self.next = None #Intialize next as None

class LinkedList(object):
    """Function to intialize node head"""
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print temp.data
            temp =temp.next

if __name__ =='__main__':
    #start with the empty list
    ll=LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third
    ll.printlist()
