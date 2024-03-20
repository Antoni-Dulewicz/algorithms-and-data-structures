def longest(text1,text2):
    n = len(text1)
    m = len(text2)
    dp = [[0 for _ in range(n+1)]for _ in range(m+1)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            tmp1 = text1[j]
            tmp2 = text2[i]
            if text1[j] == text2[i]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = dp[i][j+1]

    return dp[0][0]


text1 = "antonidulewicz"
text2 = "ntoduwiz"

res = longest(text1,text2)
print(res)

