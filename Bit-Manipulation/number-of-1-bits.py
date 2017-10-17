#Approach 1
def setbits(n):
    a = bin(n)
    a = a[2:]
    return a.count('1')

n = 4
print setbits(n)

#Approach 2
def num1bits(n):
    res = 0
    while n != 0:
        if n&1:
            res += 1

        #Shifting by one bit to the right
        n = n >> 1
    return res
