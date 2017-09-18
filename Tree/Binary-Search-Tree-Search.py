def binarySearchTree(root,key):
    if root is None or root.val == key:
        return root
    if root.val>key:
        return binarySearchTree(root.left,key)
    else:
        return binarySearchTree(root.right,key)
