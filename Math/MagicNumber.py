def sieve(n):
    prime = [True]*(n+1)
    p =2
    lis=[]
    while(p*p <n):
        if (prime[p] == True):
            for i in range(p*2,n+1,p):
                prime[i] = False
        p +=1
    for i in range(2,n):
        if prime[i]:
            lis.append(i)

    return lis
t = int(raw_input())
for i in range(t):
    n, l, r = map(int,raw_input().split())
    n = n+1
    lis = printPrime(n)
    c = 0
    for i in range(l,r+1):
        for j in lis:
            if i % j == 0:
                c += 1
                break
    print c
