'''
Given two integers find the maximum difference between two prime numbers contained in their range. For e.g. if you are given two integers 2 and 6, i.e range [2,6] inclusive, the two farthest prime numbers are 2 & 5 and the answer is 3. If there are no prime numbers in the range, print 0.
'''
from bisect import bisect_left, bisect_right
N = 10**6
def getPrimes(N):
    primes = [2]
    check = [1] * N
    for i in range(3,N,2):
        if check[i]:
            primes.append(i)
            for j in range(3*i,N,2*i):
                check[j] = 0
    return primes

primes = getPrimes(N)
t = int(raw_input())
for i in range(t):
    n1, n2 = map(int,raw_input().split())
    i1 = bisect_right(primes,n1)
    i2 = bisect_left(primes,n2)
    if i1 > 0 and primes[i1-1] == n1:
        i1 -= 1
    while i2 > 0 and primes[i2]  > n2:
        i2 -= 1

    if i2 + 1 < len(primes) and primes[i2+1] <= n2:
        i2 += 1
    p1 = primes[i1]
    p2 = primes[i2]
    #print p1, p2
    if p1 < p2:
        print p2-p1
    else:
        print 0
