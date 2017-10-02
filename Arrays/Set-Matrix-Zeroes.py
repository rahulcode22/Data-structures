#Given an m x n matrix of 0s and 1s,
#if an element is 0, set its entire row and column to 0.

def setZeroes(matrix):
    if matrix is None:
        return
    cols = [False]*len(matrix[0])
    rows = [False]*len(matrix)

    for col in range(len(matrix[0])):
        for rows in range(len(matrix)):
            if matrix[row][col] == 0:
                cols[col] = True
                rows[row] = True

    for col in range(len(matrix[0])):
        for rows in range(len(matrix)):
            if cols[col] or rows[row]:
                matrix[row][col] = 0

    return matrix
