def word_break(S,word_dict):
    n = len(S)
    n += 1
    dp = [False for _ in range(n)]
    dp[n-1] = True

    for i in range(n-2,-1,-1):
        for word in word_dict:

            word_len = len(word)
            tmp = S[i:i+word_len]
            if word == tmp:
                dp[i] = dp[i+word_len]


    return dp[0]


S = "neetcode"
word_dict = ["neet","leet","code"]
print(word_break(S,word_dict))