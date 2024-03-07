def select(T):
    n = len(T)
    p = T[0]
    q = T[n-1]
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if T[j]<T[min_idx]:
                min_idx = j
        T[min_idx],T[i]=T[i],T[min_idx]

    print(T)            
    return


T = [3,4,2,5,6,12,32,12,1,9]
select(T)