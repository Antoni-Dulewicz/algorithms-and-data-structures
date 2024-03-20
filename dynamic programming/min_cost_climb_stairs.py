def min_cost(cost):
    n = len(cost)
    dp = [cost[n-1],0]
    for i in range(n-2,-1,-1):
        curr = min(cost[i]+dp[0],cost[i]+dp[1])
        dp = [curr,dp[0]] 

    return min(dp[0],dp[1])

T = [1,100,1,1,1,100,1,1,100,1]
cost = [10,15,20]
print(min_cost(cost))


