#Taking fib of first two number
#Time complexity: O(n)
#Extra Space: O(n)
fibarray = [0, 1]
def fibonacci(n):
    if n < 0:
        raise IndexError("Please input a non-negative number")
    elif n <= len(fibarray):
        return fibarray[n-1]
    else:
        temp = fibonacci(n-1) + fibonacci(n-2)
        fibarray.append(temp)
        return temp

print fibonacci(3)
