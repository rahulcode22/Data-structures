'''
Horner’s method can be used to evaluate polynomial in O(n) time. To understand the method, let us consider the example of 2x3 – 6x2 + 2x – 1. The polynomial can be evaluated as ((2x – 6)x + 2)x – 1. The idea is to initialize result as coefficient of xn which is 2 in this case, repeatedly multiply result with x and add next coefficient to result. Finally return result.
'''
def horner(arr,n,x):
    res = arr[0]
    for i in range(1,n):
        res = res*x + arr[i]
    return res
