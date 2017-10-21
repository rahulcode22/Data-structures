'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
def rotate(self,k,head):
    if k == 0:
        return head
    count = 1
    curr = head
    while count < k and curr is not None:
        curr = curr.next
        count += 1
    if curr is None:
        return head

    kthNode = curr

    while curr.next is not None:
        curr = curr.next
    curr.next = head

    head = kthNode.next

    kthNode.next = None

    return head
