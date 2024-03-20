def roznica(S):
    max_def = -1
    n = len(S)
    for i in range(n):
        cnt_0 = 0
        cnt_1 = 0
        for j in range(i,-1,-1):
            if S[j] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1
            if cnt_0 > 0 and cnt_1 > 0:
                max_def = max(max_def,abs(cnt_1-cnt_0))
    return max_def

