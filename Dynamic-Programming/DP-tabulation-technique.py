#The tabulation technique builds a table in bottom up fashion and returns the last entry
#from the table
#For example, for the same fibonacci algo,we first calculate fib(0) then fib(1) and so on

#Illustrated below
def fib(n):
    #array declaration
    f = [0]*(n+1)
    #base case assignment
    f[1] = 1

    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = 9
print fib(n)

#Advantages:
#IT Stores the solution of subproblems.
#Table is filled on demand
#All entries are not necessarily filleds
