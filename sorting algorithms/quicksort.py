def quicksort(T,p,r):
    while p<r:
        q = partition(T,p,r)
        quicksort(T,p,q-1)
        p = q+1            #quicksort(T,q+1,r)
    return T

def partition(T,p,r):
    x = T[r]
    i = p-1
    for j in range(p,r):
        if T[j] <= x:
            i += 1
            T[i],T[j] = T[j],T[i]
    T[i+1],T[r] = T[r],T[i+1]       
    
    return i+1 


A = [4,7,23,1,5,12,4,3,54,2]
print(quicksort(A,0,len(A)-1)) 