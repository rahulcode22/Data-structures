def CompareLists(headA, headB):
    if(headA == None and headB ==None):
        return 1
    elif(headA ==None or headB ==None):
        return 0
    
    if(headA.data == headB.data):
        return CompareLists(headA.next, headB.next)
    else:
        return 0
  
