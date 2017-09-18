class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def rev(self):
        prev = None
        curr = self.head
        while(curr):
            next = curr.next
            curr.next = prev
            prev= curr
            curr = next
        self.head = prev
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head  = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next
ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
print "Original List : "
ll.printList()

print "Reversed List : "
ll.rev()
ll.printList()
