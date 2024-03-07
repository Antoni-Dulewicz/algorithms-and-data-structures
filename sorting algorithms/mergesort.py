from random import randint
def merge(T,L,R):
    l = 0
    r = 0
    for i in range(len(T)):
        if l == len(L):
            T[i]=R[r]
            r+=1
        elif r == len(R):
            T[i]=L[l]
            l+=1
        elif R[r]<L[l]:
            T[i]=R[r]
            r +=1
        else:
            T[i]=L[l]   
            l+=1
    return        
                
def mergesort(T):
    l = len(T)
    if l < 2:
        return
    mid = (l//2)
    L = T[:mid]
    R = T[mid:]
    mergesort(L)
    mergesort(R)
    merge(T,L,R)

T = [0 for _ in range(1000)]
for i in range(1000):
    T[i] = randint(1,100)

print(T)
mergesort(T)
print(T)

