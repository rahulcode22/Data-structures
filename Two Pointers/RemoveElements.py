'''
Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
Try to do it in less than linear additional space complexity.
'''
def removeElement(arr,target):
    i = 0
    j = 0
    n = len(arr)
    while i < n:
        if arr[i] != target:
            arr[j] = arr[i]
            j += 1

        i += 1
    return len(arr[0:j])

arr = [4,1,1,2,1,3]
target = 1
print removeElement(arr,target)
