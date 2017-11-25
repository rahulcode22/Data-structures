def longestPalindromeSubsequence(s):
    n = len(s)
    dp = [[0 for i in range(n)] for i in range(n)]
    #length 1 are all palindromes
    for i in range(n):
        dp[i][i] = 1

    #Length > 1
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if l == 2 and s[i] == s[j]:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    return dp[0][n-1]
print longestPalindromeSubsequence("agbdba")
