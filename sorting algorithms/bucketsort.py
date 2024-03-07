def find_max(T):
    maxi = T[0]
    for i in range(1,len(T)):
        if T[i] > maxi:
            maxi = T[i]
    return maxi     

def bucket_sort(T):
    m = find_max(T)
    n = len(T)
    size = m/n
    buckets = [[] for _ in range(n)]
    for i in range(n):
        buckets[int(T[i]//size)].append(T[i])
            
    T = []

    for bucket in buckets:
        bucket = sorted(bucket)
        T += bucket
    
    return T


T = [12,6,22,43,36,39,27]
print(bucket_sort(T))
    