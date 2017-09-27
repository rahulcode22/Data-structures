#Find All prime numbers upto a given number n
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
