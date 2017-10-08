def KMPSearch(pat,txt):
    m = len(pat)
    n = len(txt)
    #Now create a lps array that will hold the longest prefix suffix value
    lps = [0]*m
    j = 0 #index for pat
    computeLPSArray(pat,m,lps)

    i = 0 #index For txt[]

    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == m:
            print "Pattern found at index" + str(i-j)
            j = lps[j-1]
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat,m,lps):
    j = 0 #length of previous lps
    lps[0] = 0
    i = 1
    while i < m:
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]

            else:
                lps[i] = 0
                i += 1

#Now time to test
txt = "abdefgh"
pat  = "defg"
KMPSearch(pat,txt)
