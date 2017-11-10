'''
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.
'''
def gcd(a,b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
return a
