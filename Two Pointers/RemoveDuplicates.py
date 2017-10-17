'''
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, arr):
        n = len(arr)
        if n == 0 or n == 1:
            return n
        j = 0
        for i in range(n-1):
            if arr[i] != arr[i+1]:
                arr[j] = arr[i]
                j += 1
        arr[j] = arr[n-1]
        return  j+1
