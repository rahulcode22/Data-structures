'''
Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.
'''
def minXOR(arr):
    arr = sorted(arr)
    n = len(arr)
    minXor = float('inf')
    val = 0
    for i in range(n-1):
        val = arr[i]^arr[i+1]
        minXor = min(minXor,val)

    return minXor

arr = [0,4,7,9]
print minXOR(arr)
