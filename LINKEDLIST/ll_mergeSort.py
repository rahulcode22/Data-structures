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
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print temp
            temp = temp.next

def mergeLists(l1,l2):
    temp= None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp =l1
        temp.next = mergeLists(l1.next,l2)
    else:
        temp = l2
        temp.next = mergeLists(l1,l2.next)
    return temp

def mergeSort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divideLists(head)
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    head = mergeLists(l1, l2)
    return head

def divideLists(head):
    slow = head #slow is a pointer to reach the mid of linked list
    fast = head #fast is a pointer tor reach the end of linked list
    if fast:
        fast = fast.next
    while fast:
        fast = fast.next #fast is incremented twice here
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid
if __name__ == '__main__':
    ll =LinkedList()
    ll.append(20)
    ll.append(10)
    ll.append(50)
    ll.append(40)
print "Before sorting"
ll.printList()
print "after sorting"
ll.head  = mergeSort(ll.head)
ll.printList()
