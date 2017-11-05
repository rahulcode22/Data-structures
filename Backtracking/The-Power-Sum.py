'''
Find the number of ways that a given integer X, can be expressed as the sum of N the  power of unique, natural numbers.
'''
def countWaysUtil(x, n, num):
    val = x - (num**n)
    if val == 0:
        return 1
    if val < 0:
        return 0
    return countWaysUtil(val, n, num + 1) + countWaysUtil(x, n, num+1)

x = int(raw_input())
n = int(raw_input())
print countWaysUtil(x, n, 1)
