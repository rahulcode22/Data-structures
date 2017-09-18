class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None

class LinkedList:
    def __init__(self):
        self.head = None

    def detectAndRemoveLoop(self):
        slow_p  = fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            #if slow_p and fast_p meet at some point then
            #there is a loop
            if slow_p == fast_p:
                self.removeLoop(slow_p)
                return 1
            return 0

    def removeLoop(self,loop_node):
        ptr1 = loop_node
        ptr2 = loop_node

        k=1
        while(ptr1.next != ptr2):
            ptr1 = ptr1.next
            k +=1

        #Fixing one pointer to head
        ptr1 = self.head

        ptr2 = self.head
        #Add another pointer to k nodes after head
        for i in range(k):
            ptr2 = ptr2.next

        #Move both pointer at same pace ,they will meet at loop starting point
        while (ptr2 != ptr1):
             ptr1 = ptr1.next
             ptr2 = ptr2.next


        #get pointer to last node
        ptr2 = ptr2.next
        while(ptr2.next != ptr1):
            ptr2 = ptr2.next

        ptr2.next = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next


ll = LinkedList()
ll.push(10)
ll.push(3)
ll.push(15)
ll.push(20)
ll.push(50)

#creating a loop for testing
ll.head.next.next.next.next.next = ll.head.next.next

ll.detectAndRemoveLoop()

print "Linked List after removing Loop"
ll.printList()
