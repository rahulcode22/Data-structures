'''
Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.
'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, matrix):

        lis = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lis.append(matrix[i][j])

        lis.sort()
        return lis[len(lis)/2]
