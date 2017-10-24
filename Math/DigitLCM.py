'''
Given a number n, find LCM of its digits.
'''
def gcd(x,y):
    while y:
        x, y = y, x%y
    return x

def lcm(x,y):
    lcm_ = x*y//gcd(x,y)
    return lcm_

def digitLCM(n):
    lcmd = 1
    while n > 0:
        lcmd = lcm(n%10, lcmd)
        if lcmd == 0:
            return 0
        n = n/10
    return lcmd

n = 397
print digitLCM(n)
