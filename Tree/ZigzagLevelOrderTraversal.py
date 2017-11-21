def zizZagLevelOrder(root):
    if not root:
        return []
    res = []
    temp = []
    stack = [root]
    flag = 1
    while stack:
        for i in range(len(stack)):
            node = stack.pop(0)
            temp += [node.val]
            if node.left:
                stack += [node.left]
            if node.right:
                stack += [node.right]
        res += [temp[::flag]]
        temp = []
        flag *= -1
    return res

print zizZagLevelOrder([3, 9, 20, None, None, 15, 7])
