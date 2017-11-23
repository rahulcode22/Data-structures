def coinChange(coins,total):
    m = [[0 for i in range(total+1)] for i in range(len(coins)+1)]

    for i in range(r+1):
        m[0][i] = i

    for row in range(1,len(coins)+1):
        for col in range(1,n+1):
            if coins[row-1] == col:
                m[row][col] = 1
            #Coins[c-1] can't be included
        elif coins[row-1] > col:
                m[row][col] = m[row-1][col]
            #coin[c-1] cn be used
            else:
                m[row][col] = min(m[row-1][col],1+m[row][col-coins[row-1]])
    return m[-1][-1]
