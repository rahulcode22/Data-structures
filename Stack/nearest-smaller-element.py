'''

Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.


'''
def smaller(arr):
    res = []
    stack = []
    for i in range(len(arr)):
        while len(stack) != 0 and stack[-1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])

        stack.append(arr[i])
    return res

arr = [1,3,0,2,5]
print smaller(arr)
