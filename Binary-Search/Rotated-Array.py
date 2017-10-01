'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array will not contain duplicates.
'''
def findMin(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        low = 0
        high = len(arr)-1
        mid = (low+high)/2
        if arr[mid] > arr[high]:
            return findMin(arr[mid+1:])
        elif arr[mid] < arr[high]:
            return findMin(arr[:mid+1])
arr = [4,5,6,7,0,1,2]
print findMin(arr)
