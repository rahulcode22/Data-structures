class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        printGivenOrder(root,i)

def printGivenOrder(root,level):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.val),
    elif level >1:
        printGivenOrder(root.left,level-1)
        printGivenOrder(root.right,level-1)

def height(node):
    if node is None:
        return 0
    else:
        #Compute Height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "Level order traversal of binary tree is -"
printLevelOrder(root)
