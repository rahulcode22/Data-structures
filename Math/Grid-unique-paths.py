'''A robot is located at the top-left corner of an A x B grid
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?


'''
def uniquePaths(a,b):
    if a ==1 or b == 1:
        return 1
    return uniquePaths(a-1,b) +uniquePaths(a,b-1)
a = 3
b = 3
print uniquePaths(a,b)
