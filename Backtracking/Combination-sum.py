from itertools import groupby
def combinationSum(self,arr, target):
    res = []
    arr = sorted(arr)
    def dfs(remain, stack):
        if remain == 0:
            res.append(stack)
            return

        for item in arr:
            if item > remain:
                break
            if stack and item < stack[-1]:
                continue
            else:
                dfs(remain-item,stack + [item])
    dfs(target, [])
    result = list(k for k,_ in groupby(res))
    return result
arr = [ 8, 10, 6, 11, 1, 16, 8 ]
target = 28
print combinationSum(arr,target)
