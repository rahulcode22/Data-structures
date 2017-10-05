'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, arr, target):

        floor_index = 0
        ceiling_index = len(arr) - 1
        if len(arr) == 1 and arr[0] == target:
            return 0
        if arr[ceiling_index-1] < target:
            return ceiling_index + 1

        while floor_index < ceiling_index:
            mid = (floor_index + ceiling_index)/2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                ceiling_index = mid-1
                ans = mid -1
            else:
                floor_index = mid + 1
                ans = mid + 1
        if arr[ans] < target:
            return ans + 1
        else:
            return ans
