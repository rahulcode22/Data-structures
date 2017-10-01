'''Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].'''
def searchForARange(arr,target):
    n = len(arr)
    first_occurence = -1
    floor_index = 0
    ceiling_index = n-1
    while floor_index < ceiling_index:
        mid = (floor_index + ceiling_index)/2
        if arr[mid] == target:
            first_occurence = mid
            ceiling_index = mid-1
        elif arr[mid] >  target:
            ceiling_index  = mid -1
        else:
            floor_index = mid + 1
    second_occurence = -1
    floor_index = first_occurence
    ceiling_index = n-1
    while floor_index <= ceiling_index:
        mid = (floor_index +ceiling_index)/2
        if arr[mid] == target:
            second_occurence  = mid
            floor_index = mid + 1
        else:
            ceiling_index = mid - 1
    return first_occurence-1,second_occurence

arr = [5,7,7,8,8,10]
target = 7
print searchForARange(arr,target)
