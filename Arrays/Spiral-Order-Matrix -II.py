#Given an integer n, generate a square matrix 
#filled with elements from 1 to n2 in spiral order.
def generateMatrix(n):
    matrix = [[0 for _ in xrange(n)] for _ in xrange(n)]

    l, r, t, b, c = 0, n-1, 0, n-1, 1
    dir = 0

    while l<=r and l<=r:
        if dir == 0:
            for i in range(l,r+1):
                matrix[t][i] = c
                c +=1
            t = t+1
            dir = 1
        elif dir == 1:
            for i in range(t,b+1):
                matrix[i][r] = c
                c +=1
            r = r-1
            dir = 2
        elif dir == 2:
            for i in range(r,l-1,-1):
                matrix[b][i] = c
                c +=1
            b =b-1
            dir = 3
        elif dir == 3:
            for i in range(b,t-1,-1):
                matrix[i][l] = c
                c +=1
            l = l+1
            dir = 0
        else:
            print "Error"

    return matrix

n =3
print generateMatrix(n)
