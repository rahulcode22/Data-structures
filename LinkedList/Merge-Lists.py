'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
'''
def merge(h1,h2):
    if None in (h1,h2):
        return h1 or h2
    dummy = head = ListNode(0)
    while h1 and h2:
        if h1.val < h2.val:
            head.next = h1
            head = h1
            h1 = h1.next
        else:
            head.next = h2
            head = h2
            h2 = h2.next

    head.next = h1 or h2
    return dummy.next
