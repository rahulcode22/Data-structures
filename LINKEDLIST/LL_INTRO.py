
#uses python2
Class Node:
    def __init__(self,data):
        self.data=data #intializes data
        self.next=None
Class Linkedlist:
    def __init__(self):
        self.head=None #initializes head
#Main Part
if __name__ =='__main__':
    ll=Linkedlist()
    ll.head=Node(1)
    ll.second=Node(2)
    ll.third=Node(3)
    ll.head.next=second
    ll.second.next=third
    
    
