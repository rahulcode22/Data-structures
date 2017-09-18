#There are two ways to store the values so that these values can be reused
#Method -1) Memoization
        #   ->It is similar to recursive version with  a small modification that
        #       it looks into the lookup table before computing solution

#Fibonnaci Example memoized version
def fib(n, lookup):
    #Base Case
    if n == 0 or n == 1:
        lookup[n] = n

    #if the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n-1,lookup) + fib(n-2.lookup)

    #Return the value corresponding to that value of n
    return lookup[n]

n = 34
lookup = [None]*101

print fib(n,lookup)
