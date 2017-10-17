'''Sort a linked list in O(n log n) time using constant space complexity.'''
def merge(self,h1,h2):
    dummy = tail = ListNode(0)
    while h1 and h2:
        if h1.val < h2.val:
            tail.next = h1
            tail = h1
            h1 = h1.next
        else:
            tail.next = h2
            tail = h2
            h2 = h2.next
    tail.next = h1 or h2
    return dummy.next
def sortList(head):
    if head or head.next:
        return head
    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next
    prev.next = None
    return self.merge(self.sort(head),self.sort(slow))
