class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    """Inserting node at front """
    def push_front(self,new_data):
        new_node = Node(new_data) #creating new Node
        new_node.next = self.head
        self.head =new_node
    """Inserting node after a given node"""
    def push_after(self,prev_node,new_data):
        if prev_node is None:
            print "no previous node"
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    """Inserting node at the end of LinkedList"""
    def push_end(self,new_data):
        new_node = Node(new_data)
        last = self.head
        while(last.next):
            last=last.next
        last.next = new_node
    def printlist(self):
        temp = self.head
        while(temp):
            print temp.data
            temp =temp.next
if __name__ =='__main__':
    ll=LinkedList()
    ll.push_front(1)
    ll.push_after(ll.head.next,8)
    ll.push_end(9)
    print "Created LinkedList list is :"
    ll.printlist()
