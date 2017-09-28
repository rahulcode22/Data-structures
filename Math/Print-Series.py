'''
A number (N1)
A number (N2)
Write a function which prints first N1 terms of the series 3n + 2 which are not multiples of N2.
'''
n1 = int(raw_input())
n2 = int(raw_input())
i = 1
c = 0
while(i !=0):
    num = 3*i + 2
    if num%n2 != 0:
        print num
        c +=1
    if c == n1:
        break

    i +=1
