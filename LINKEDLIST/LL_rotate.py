class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head  =new_node

    def rotate(self,k):
        curr = self.head
        count = 1

        while (count<k and curr is not None):
            curr =curr.next
            count +=1

        if curr is None:
            return


        kthNode = curr
        #REach to the lst node
        while (curr.next is not None):
            curr = curr.next

        curr.next = self.head

        self.head = kthNode.next

        kthNode.next = None

    def printList(self):
        temp = self.head
        while (temp):
            print temp.data
            temp = temp.next



ll = LinkedList()

for i in range(60, 0, -10):
    ll.append(i)

print "Given Linked List: "
ll.printList()
ll.rotate(4)

print "Rotated linked list is :"
ll.printList()

