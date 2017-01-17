#uses python2
def reverse(self):
    prev=None
    curr=self.head
    while(curr is not None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    self.head=prev
