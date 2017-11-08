'''
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;
Example :

Input :
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5
         With 10 from A, 15 from B and 10 from C.
'''
def minimize(a,b,c):
    i, j, k = 0, 0, 0
    diff = float('inf')
    res_i, res_j, res_k = 0, 0, 0
    while i <len(a) and j <len(b) and k < len(c):
        maximum = max(abs(a[i]-b[j]),abs(b[j]-c[k]),abs(c[k]-a[i]))
        minimum = min(a[i],b[j],c[k])
        if maximum  < diff:
            res_i = i
            res_j = j
            res_k = k
            diff = maximum
        if diff == 0:
            break
        if a[i] == minimum:
            i += 1
        elif b[j] == minimum:
            j += 1
        else:
            k += 1
    return diff

a = [1,4,10]
b = [2,15,20]
c = [10,12]
print minimize(a,b,c)
