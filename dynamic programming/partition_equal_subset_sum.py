def partition(nums):
    sums = [0]
    half = 0
    for i in range(len(nums)):
        half += nums[i]
    half /= 2
    n = len(nums)
    for i in range(n-1,-1,-1):
        tmp = []
        for j in range(len(sums)):
            if (nums[i] + sums[j]) not in sums:
                tmp += [nums[i] + sums[j]]
                if nums[i] + sums[j] == half:
                    return True
        sums += tmp

    return False


nums = [1,5,11,5]
print(partition(nums))