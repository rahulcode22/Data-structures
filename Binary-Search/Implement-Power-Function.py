'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative
'''
def pow(self, x, n, d):
    result = 1
    base = x % d
    while n > 0:
        if n % 2 == 1:
            result = (result*base) % d
        n = n >> 1
        base = (base*base)%d
    return result%d
