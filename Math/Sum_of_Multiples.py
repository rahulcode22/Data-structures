'''Given a number a and limit N. Find the sum of multiple of a upto N.'''
#Simple Iterative O(n) Approach
def sumUpto(a,n):
    sum_ = 0
    i = a
    while i <= n:
        sum_ += i
        i += a
    return sum_

print sumUpto(7,49)


#Another O(1) Approach
def sumUpto(a,n):
    m = n/a
    sum_ = m*(m+1)/2
    ans = a*sum_
    return ans

print sumUpto(7,49)
