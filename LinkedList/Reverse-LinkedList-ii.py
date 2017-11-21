def reverseBetween(head, m, n):
    if m == n:
        return head
    dummyNode = ListNode(0)
    dummyNode.next = head
    prev = dummyNode

    for i in range(m-1):
        prev = prev.next

    rev = None
    curr = prev.next

    for i in range(n-m+1):
        next = curr.next
        curr.next = rev
        rev = curr
        curr = next
    prev.next.next = curr
    prev.next = reverse
    return dummyNode.next
