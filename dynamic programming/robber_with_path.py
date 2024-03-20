def robber(T):
    n = len(T)
    dp = [0 for _ in range(n)]
    dp[0] = T[0]
    dp[1] = T[1] 
    parent = [-1 for _ in range(n)]
    
    
    for i in range(2,n):
        if dp[i-1] > dp[i-2] + T[i]:
            dp[i] = dp[i-1]
            parent[i] = parent[i-1]
        else:
            dp[i] = dp[i-2] + T[i]
            j = i - 2 
            while j >= 0 and dp[j] == dp[j-1]:
                j -= 1
            parent[i] = j
            
    path = []
    idx = n-1
    path += [n-1]
    while parent[idx] !=  -1:
        path += [parent[idx]]
        idx = parent[idx]
    
    return dp[n-1],path,parent
T = [2,5,8,3,4,5,1,3]
#T = [1, 100, 1, 1, 1, 10, 2, 2, 100, 3, 5]
T = [1,3,-1,0,2,-1,5,1]
print(robber(T))