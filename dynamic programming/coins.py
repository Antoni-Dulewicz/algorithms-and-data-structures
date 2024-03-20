"""Na ile sposobow mozna zapisac wartosc uzywajac sumy podanych
monet"""

def how_may_ways(coins,amount):
    n = len(coins)
    m = amount+1
    tab_amout = [amount-i for i in range(amount+1)]
    dp = [[0 for _ in range(m)] for _ in range(n+1)]
    for i in range(n):
        dp[i][m-1] = 1
    for j in range(m-2,-1,-1):
        for i in range(n-1,-1,-1):
            cell_amount =  tab_amout[j] - coins[i]
            if cell_amount >= 0:
                dp[i][j] = dp[i][m-cell_amount-1] + dp[i+1][j]

    for w in range(n):
        print(dp[w])
    return dp[0][0]

# mniejesza zlozonosc pamieciowa(tutaj O(n), tam O(mn)), taka sama zlozonosc czasowa (O(m*n)):
def other_solution(coins,amount):
    n = len(coins)
    dp = [0 for _ in range(amount+1)]
    dp[0] = 1
    for i in range(n-1,-1,-1):
        newDP = [0 for _ in range(amount+1)]
        newDP[0] = 1

        for a in range(1,amount+1):
            tmp_idx = a - coins[i]
            if tmp_idx >= 0:
                newDP[a] = newDP[tmp_idx] + dp[a]
        dp = newDP
    return dp[amount]


coins = [1,2,4]
amount = 5
print(other_solution(coins,amount))