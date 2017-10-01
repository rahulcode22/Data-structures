def findCount(arr,target):
    n = len(arr)
    floor_index = 0
    ceiling_index = n-1
    first_occurence = -1
    while floor_index < ceiling_index:
        mid = (floor_index + ceiling_index)/2
        if arr[mid] == target:
            first_occurence = mid
            high = mid-1
        elif arr[mid] > target:
            ceiling_index = mid-1
        else:
            floor_index = mid+1

    if first_occurence == -1:
        return 0

    floor_index = first_occurence
    high = n-1
    second_occurence = -1
    while floor_index < ceiling_index:
        mid = (floor_index + ceiling_index)/2
        if arr[mid] == target:
            second_occurence = mid
            low = mid + 1
        else:
            high = mid -1
    return second_occurence - first_occurence + 1

'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, arr, x):

        def first(arr,low,high,x):

            if (high >= low):

                mid = (low+high)/2
                if (mid == 0 or x >arr[mid-1]) and arr[mid] == x:
                    return mid
                elif x > arr[mid]:
                    return first(arr,(mid+1),high,x)
                else:
                    return first(arr,low,(mid-1),x)
            return 0
        def last(arr,low,high,x):

            if high >= low:
                mid = (low+high)/2
                if (mid == len(arr)-1 or x < arr[mid+1]) and arr[mid] == x:
                    return mid
                elif x < arr[mid]:
                    return last(arr,low,(mid-1),x)
                else:
                    return last(arr,(mid+1),high,x)
            return 0

        i = first(arr,0,len(arr)-1,x)
        if i == 0:
            return i
        j = last(arr,i,len(arr)-1,x)
        return j-i+1

'''
