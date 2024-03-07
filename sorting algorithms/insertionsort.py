def insertSort(T):
    for i in range(1,len(T)):
        curr = T[i]
        j = i-1
        while T[j] > curr and j >= 0:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = curr
    print(T)
T = [4,3,8,2,1]
insertSort(T)

