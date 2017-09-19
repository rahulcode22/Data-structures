#Given an array of real numbers greater than zero in form of strings.
#Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
#Return 1 for true or 0 for false.
def triplet(arr):
    arr.sort()
    n = len(arr)
    i = n-1

    while(i>=0):
        j = 0
        k = i-1
        if i == j or k == j:
            return 0

        elif arr[i]+arr[j]+arr[k]>1 and arr[i]+arr[j]+arr[k]<2:
            print arr[i]+arr[j]+arr[k]
        elif arr[i]+arr[j]+arr[k]>=2:
            k -=1
        else:
            j +=1
        i -=1

    return 0

#Method 2
def solve(self, A):
    A = sorted(A)

    i = 0
    j = len(A)-1
    while i < j-1:
        s = float(A[i]) + float(A[j])
        if i + 1 < len(A) - 1:
            three = s + float(A[i+1])
            if three > 1 and three < 2:
                return 1
            elif three < 1:
                i += 1
            else:
                j -= 1
    return 0
