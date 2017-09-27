'''Given a number n ,verify if n is prime or not'''
def isPrime(self, n):
    if n == 2 or n == 3:
        return 1
    if n== 1:
        return 0
    if (n%2 == 0 or n%3 == 0):
        return 0

    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i ==0 or n%(i+2) ==0:
            return 0
    return 1
