'''
Given a square matrix of order n*n, we need to print elements of the matrix in Z form
'''
def PrintZ(arr):
    #Printing first row
    for i in range(0,len(arr)):
        print arr[0][i],

    #Printing diagonal elements
    k = 1
    for i in range(0,n):
        for j in range(n,0,-1):
            if (j == n-k):
                print arr[i][j],
                break
        k +=1
    i = n-1
    for j in range(0,n):
        print arr[i][j],
