def path(m,n):
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        dp[m-1][i] = 1

    for i in range(m):
        dp[i][n-1] = 1

    for i in range(m-2,-1,-1):
        for j in range(n-2,-1,-1):
            dp[i][j] = max(dp[i][j+1] + dp[i+1][j],dp[i][j])
    
    return dp

m = 3
n = 7

print(path(m,n))