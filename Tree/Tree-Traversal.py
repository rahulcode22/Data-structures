class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def printInorder(root):
    if root:

        #Recur on left child
        printInorder(root.left)
        #Print Root data
        print (root.val),
        #Recur on right child
        printInorder(root.right)

def printPostorder(root):
    if root:
        #First Recur on left child
        printPostorder(root.left)

        printPostorder(root.right)

        print (root.val),

def printPreorder(root):
    if root:
        print root.val,
        printPreorder(root.left)
        printPreorder(root.right)

# Driver code
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
print "Preorder traversal of binary tree is"
printPreorder(root)

print "\nInorder traversal of binary tree is"
printInorder(root)

print "\nPostorder traversal of binary tree is"
printPostorder(root)
