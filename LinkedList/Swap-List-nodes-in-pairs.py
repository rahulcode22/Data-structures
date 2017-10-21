'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
#Approach 1
def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next


#Approach 2
def swapPairs(head):
    curr = head
    nxt = head.next
    while curr and nxt:
        curr.val, nxt.val = nxt.val, curr.val
        curr = nxt.next
        if curr:
            nxt = curr.next
    return head
