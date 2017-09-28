'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.Don't return anything.
'''
def RearrangeArray(arr):
    for i in range(len(arr)):
        arr[i] +=(arr[arr[i]]%n)*n
    for i in range(len(arr)):
        arr[i] = arr[i]/n
