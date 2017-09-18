#Iterative solution for finding length of a LinkedList
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def getCount(self):
        count = 0;
        curr = self.head
        while(curr):
            curr = curr.next
            count +=1
        return count

if __name__ =='__main__':
    ll =LinkedList();
    ll.push(1)
    ll.push(2)
    ll.push(3)

    print 'count of nodes is : ', ll.getCount()

#Recursive solution for finding length of a LinkedList
