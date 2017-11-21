#Complexity O(M+N)
def isInterleaved(a,b,c):
    i, j, k = 0, 0, 0

    while k !=len(c)-1:
        if a[i] == c[k]:
            i += 1
        elif b[j] == c[k]:
            j += 1
        else:
            return 0

        k += 1
    if a[i-1] or b[j-1]:
        return 0
    return 1

a = "AB"
b = "CD"
c = "ACBG"
if isInterleaved(a,b,c) == 1:
    print c + "is Interleaved of "+ a + " and " + b
else:
    print "Not Interleaved"


#Dynamic Approach
def isInterleaved(a,b,c):
    m = len(a)
    n = len(b)

    table = [[False for i in range(n+1)] for i in range(m+1)]

    if m+n != len(c):
        return False

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                table[i][j] = True
            elif i == 0 and (b[j-1] == c[j-1]):
                table[i][j] = table[i][j-1]
            elif j == 0 and a[i-1] == c[i-1]:
                table[i][j] = table[i-1][j]
            elif a[i-1] == c[i+j-1] and b[j-1] != c[i+j-1]:
                table[i][j] = table[i-1][j]
            elif a[i-1] != c[i+j-1] and b[j-1] == c[i+j-1]:
                table[i][j] = table[i][j-1]
            elif a[i-1] == c[i+j-1] and b[j-1] == c[i+j-1]:
                table[i][j] = table[i-1][j] or table[i][j-1]
    return table[m][n]
