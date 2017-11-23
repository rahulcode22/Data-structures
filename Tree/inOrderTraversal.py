def inOrder(root):
    curr = root
    s = []
    done = 0
    ans = []
    while (not done):
        if curr is not None:
            s.append(curr)
            curr = curr.left
        else:
            if len(s) > 0:
                curr = s.pop()
                ans.append(curr.data)
                curr = curr.right
            else:
                done = 1
