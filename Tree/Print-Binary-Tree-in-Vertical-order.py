class Node:
    def __init__(self,data):
        self.key =data
        self.left = None
        delf.right = None

def getVerticalOrder(root,hd,m):
    if root is None:
        return

    try:
        m[hd].append(root.key)
    except:
        m[hd] = [root.key]

    #Stores nodes in left subtree
    getVerticalOrder(root.left,hd-1,m)
    #Stores nodes in right subtree
    getVerticalOrder(root.right,hd+1,m)

def printVerticalOrder(root):
    m = dict()
    hd = 0
    getVerticalOrder(root,hd,m)

    for index,value in enumerate(sorted(m)):
        for i in m[value]:
            print i,
        print

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print "Vertical order traversal is"
printVerticalOrder(root)
