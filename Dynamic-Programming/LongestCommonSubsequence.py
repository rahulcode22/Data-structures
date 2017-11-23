#Recursive Approach
def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    if  m == 0 or n ==0 :
        return 0
    elif s1[m-1] == s2[n-2]:
        return 1 + lcs(s1[:m-1], s2[:n-1])
    else:
        return max(lcs(s1,s2[:n-1]), lcs(s1[:m-1],s2))

x = "AGGTAB"
y = "GXTXAYB"
print "Length of lcs is " , lcs(x, y)

#Dynamic Approach
def lcs(x, y):
    m = len(x)
    n = len(y)
    table = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif x[i-1] == y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])
    return table[m][n]
x = "AGGTAB"
y = "GXTXAYB"
print "Length is ", lcs(x,y)
