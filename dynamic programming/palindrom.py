def palindrom(S):
    n = len(S)
    parent = [[(0,0) for _ in range(n)] for _ in range(n)]
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    for j in range(1,n):
        for i in range(n-j):
            if S[i] == S[i+j]:
                dp[i][i+j] = dp[i+1][i+j-1]
            else:
                dp[i][j] = dp[i+1][i+j] or  dp[i][i+j-1]
    
    return dp
    





S = 'aacaccabcc'
S1 = 'babcbab'
dp= palindrom(S)
print(*dp,sep='\n')
