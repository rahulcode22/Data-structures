def has_cycle(head):
    slow=head
    fast=head
    while(slow and fast and fast.next is not None):
        slow=slow.next
        fast=fast.next.next
        if (slow==fast):
            return True
        else:
            return False
