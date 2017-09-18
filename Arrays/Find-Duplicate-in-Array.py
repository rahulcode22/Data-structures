#Given a read only array of n + 1 integers between 1 and n,
#find one number that repeats in linear time using less than O(n) space
#and traversing the stream sequentially O(1) times
def repeatedNumber(self, A):

    A = list(A)
    A.sort()

    for i in range(len(A)-1):
        if A[i+1] - A[i] !=1:
            return A[i]
    return -1
