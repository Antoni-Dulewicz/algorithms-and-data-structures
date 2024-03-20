from math import inf
def falisz(T):
    n = len(T)
    dp = [[(inf,inf) for _ in range(n)] for _ in range(n)]
    dp[0][0] = (0,0)

    for i in range(1,n):
        from_up = inf
        if i - 1 >= 0:
            from_up = min(dp[i-1][0][0] + T[i-1][0],dp[i-1][0][1] + T[i-1][0])
        dp[i][0] = (inf,from_up)

    for j in range(1,n):
        for i in range(n):
            from_left = inf
            from_up = inf
            if i - 1 >= 0:
                from_up = min(dp[i-1][j][0] + T[i-1][j],dp[i-1][j][1] + T[i-1][j])
            if j - 1 >= 0:
                from_left = min(dp[i][j-1][0] + T[i][j-1],dp[i][j-1][1] + T[i][j-1])
            
            dp[i][j] = (from_left,from_up)

    return min(dp[n-1][n-1][0],dp[n-1][n-1][1])



T = [
 [0, 5, 4, 3],
 [2, 1, 3, 2],
 [8, 2, 5, 1],
 [4, 3, 2, 0]
]
print(falisz(T))