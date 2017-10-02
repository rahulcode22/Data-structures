'''
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
'''
import math
def power(n):
    if n == 1:
        return True
    for x in range(2,int(math.sqrt(n))+1):
        y = 2
        while( x**y <= n):
            if x**y == n:
                return True
            else:
                y += 1
    return False

print power(8)
