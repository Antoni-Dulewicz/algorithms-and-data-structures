def max_prod(nums):
    res = max(nums)
    currMin, currMax = 1,1

    for n in nums:
        if n == 0:
            currMin,currMax = 1,1
            continue
        tmp = currMax * n
        currMax = max(n*currMax,n*currMin,n)
        currMin = min(tmp,n * currMin, n)
        res = max(res,currMax)
    return res


tab = [2,3,-2,4]
print(max_prod(tab))