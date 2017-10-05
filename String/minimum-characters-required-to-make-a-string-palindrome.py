'''
You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
'''
def computeLPSArray(pat):
    j = 0
    i = 1
    m = len(pat)
    lps = [0]*m
    lps[0] = 0
    while i < m:

        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0 and pat[i] != pat[j]:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

st = "ABC"
rev = st + "$" + st[::-1]
lps = computeLPSArray(rev)
print len(st) - lps[len(lps)-1]
