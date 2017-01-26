#insertion at front
def insertafter(head,data):
    new_node=node(data)
    new_node.next=head
    new_node.prev=None
    if head is not None:
        head.prev=new_node
    head=new_node
    
#Add a node after a given node
def insertafter(prev_node,data):
    if prev_node is None:
        return
    #Allocate new node
    new_node=node(data)
    #make ne xt of new_node as next of prev_node
    new_node.next=prev_node.next
    #make next of prev_node as next of new_node
    prev_node.next=new_node.next
    #make prev_node as previous of new_node
    new_node.prev=prev_node
    if (new_node.next is not None):
        new_node.next.prev=new_node
    
    
