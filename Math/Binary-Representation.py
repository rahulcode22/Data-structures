#Given a number N >= 0, find its representation in binary.

    def findDigitsInBinary(self, n):
        lis = [0]*n
        i = 0
        if n == 1:

            return 1
        if n == 0:
            return 0
        while(n>0):
            lis[i] = n%2
            n=n/2
            i +=1
        lis = lis[:i]

        a = ''.join(map(str,lis[::-1]))
        return a
        
