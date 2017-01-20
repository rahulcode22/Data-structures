#uses python2

#Given key to be deleted
def delete(key):
    temp=head
    #if head itself holds the key
    while(temp is not None):
        if (temp.data ==key):
            head=temp.next
            temp=None
            return
        while(temp is not None):
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next
        if (temp is not None):
            return
        prev.next=temp.next
        temp=None


#delete a node at given poisition
def delete(position):
    if head is None:
        return
    temp=head
    #previous node of the node to be deleted
    for i in range(position-1):
        temp=temp.next
        if temp is None:
            break
    #if position is more than no of nodes
    if temp.next is None:
        return
    #next pointer which stores next node of the node to be deleted
    next=temp.next.next
    temp.next=None
    temp.next=next
    
    
        
    
