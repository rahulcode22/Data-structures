def GetNode(head, position):
    index=0
    temp=head
    res=head
    while(temp is not None):
        temp=temp.next
        
        if (index > position):
            
            res=res.next
        index=index+1
    return res.data
