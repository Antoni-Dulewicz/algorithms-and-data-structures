from math import inf
def ksuma(T,k):
    n = len(T)
    sum = 0
    to_add = inf
    
    dp = [0 for _ in range(n)]
    for i in range(n):
        if i < k:
            dp[i] = T[i]
        else:
            for j in range(i-k,i):
                to_add = min(to_add,dp[j])
            dp[i] = T[i] + to_add
    
    return dp
            


T = [1, 2, 3, 4, 6, 15, 8, 7]

#T = [1, 6, 45, 6, 25, 2, 49, 8, 21, 36]
print(ksuma(T,4))