class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printNthFromEnd(self,n):
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        if (self.head is not None):
            while(count < n):
                ref_ptr = ref_ptr.next
                count += 1
        while (ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        return main_ptr.data

ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(35)
print ll.printNthFromEnd(4)
