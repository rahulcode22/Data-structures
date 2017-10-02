'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
def sortedarraySearch(arr):
    floor_index = 0
    ceiling_index = len(arr) - 1
    while floor_index < ceiling_index:
        mid = (floor_index + ceiling_index)/2
        if arr[mid] > ceiling_index:
            floor_index =mid + 1
        else:
            ceiling_index = mid - 1
    arr = arr[floor_index:] + arr[:floor_index]
    return arr

def findIndex(arr,target):

    arr = sortedarraySearch(arr)
    floor_index = 0
    ceiling_index =len(arr)-1
    while floor_index < ceiling_index:
        mid = (floor_index + ceiling_index)/2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            ceiling_index = mid-1
        else:
            floor_index = mid + 1
