from random import randint

def partition(T,p,r):
    n = len(T)
    tmp = randint(p,r)
    x = T[r]
    i = p - 1
    for j in range(p,r):
        if T[j] <= x:
            i += 1
            T[j],T[i] = T[i],T[j]
    T[i+1],T[r] = T[r],T[i+1]
    
    return i + 1

def quicksort(T,p,r):
    while p < r:
        q = partition(T,p,r)
        if q - p < r - q:
            quicksort(T,p,q-1)
            p = q + 1
        else:
            quicksort(T,q+1,r)
            r = q - 1 

def quicksort_itr(T):
    stack = []
    stack.append((0,len(T)-1))
    while stack:
        p,r = stack.pop()
        if r - p >0:
            q = partition(T,p,r)
            stack.append((p,q-1))
            stack.append((q+1,r))
    return T


T = [0 for _ in range(20)]
for i in range(20):
    T[i] = randint(1,20)

print(T)
quicksort(T,0,len(T)-1)
print(T)
