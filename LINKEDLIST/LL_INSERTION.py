#uses python2

#At Front
def push(new_data):
    new_node=Node(new_data)
    new_node.next=head
    head=new_node
    
#After a given Node
    def push(new_data,prev):
        if prev is None:
            return
        new_node=Node(new_data)
        new_node.next=prev.next
        prev.next=new_node

#At the end
    def push(new_data):
        new_node=Node(new_data)
        if head is None:
            head=new_node
            return head
        last=head
        while(last.next):
            last=last.next
        last.next=new_node
    
