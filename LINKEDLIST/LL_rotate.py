#Following code rotate a linked list counter-clockwise from given kth node.


def rotate(k):
    if k=0:
        return
    current=head
    count=1
    while(current<k and current is not None):
        current=current.next
        count=count+1
    kthnode=current
    while(current.next is not None):
        current=current.next
    current.next =head
    head=kthnode.next
    kthnode.next=None
        
