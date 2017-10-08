'''
Given two binary strings, return their sum (also a binary string).
'''
def binarySum(a,b):
    n1 = len(a)
    n2 = len(b)
    if n1 > n2:
        b = "0"*(n1-n2) + b
    elif n2 > n1:
        a = "0"*(n2-n1) + a
    carry = 0
    a = list(a)
    b = list(b)
    for i in range(n2-1,-1,-1):
        if (a[i] == b[i]) and a[i] == '0':
            a[i] = str(0+carry)
            carry = 0
        elif (a[i] == b[i]) and a[i] == '1':
            a[i] = str(0 + carry)
            carry = 1
        else:
            if carry == 1:
                a[i] = str(0)
                carry = 1
            else:
                a[i] = str(1)
                carry = 0
    if carry == 1:
        a = ["1"] + a

    return ''.join(a)

a = "1110000000010110111010100100111"
b = "101001"

print binarySum(a,b)


'''
Another Approach
'''
def add(a,b):
    a = int(a,2)
    b = int(b,2)
    c = bin(a+b)[2:]
    return c
