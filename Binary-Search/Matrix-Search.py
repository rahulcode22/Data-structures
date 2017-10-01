'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
->Integers in each row are sorted from left to right.
->The first integer of each row is greater than or equal to the last integer of the previous row.
'''
    def searchMatrix(self, arr, target):

        n = len(arr)

        if len(arr) == 1:
            if arr[0][0] == target:
                return 1
            else:
                return 0
        for i in arr:

            floor_index = 0
            ceiling_index = len(arr[0]) - 1
            while floor_index <=ceiling_index:
                mid = (floor_index + ceiling_index)/2
                if i[mid] == target:
                    return 1
                elif i[mid] > target:
                    ceiling_index = mid-1
                else:
                    floor_index = mid + 1
        return 0
