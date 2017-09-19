#Given an integer array, 
#find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
#If such an integer is found return 1 else return -1.
    def solve(self, A):
        inputSize = len(A)
        A.sort()
        start = A[0]
        for i in xrange(inputSize):
            if (start != A[i]) and (start == (inputSize - i)):
                return 1
            start = A[i]
        if start == 0:
            return 1
        return -1
