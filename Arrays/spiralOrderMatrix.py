#Given a matrix of m * n elements (m rows, n columns),
#return all elements of the matrix in spiral order.
    def spiralOrder(self, A):
        result = []
        m = len(A)
        n = len(A[0])
        ## Actual code to populate result
        t=0
        b=m-1
        l=0
        r=n-1
        dir = 0
        while (t<=b and l<=r):
            if dir ==0:
                for i in range(l,r+1):
                    result.append(A[t][i])
                t =t+1
                dir = 1
            elif (dir ==1):
                for i in range(t,b+1):
                    result.append(A[i][r])
                r=r-1
                dir = 2
            elif (dir == 2):
                for i in range(r,l-1,-1):
                    result.append(A[b][i])
                b=b-1
                dir = 3
            elif (dir ==3):
                for i in range(b,t-1,-1):
                    result.append(A[i][l])
                l=l+1
                dir =0
            else:
                print "Error"
        return result
