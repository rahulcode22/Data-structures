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
        
    
