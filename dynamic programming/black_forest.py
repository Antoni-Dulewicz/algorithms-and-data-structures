from random import randint
from functools import cache
N = 20
C = [randint(2,7) for _ in range(N)]

@cache
def f(k,b):
    if k < 0: return 0
    if b: return f(k-1,False) + C[k]
    return max(f(k-1,True),f(k-1,False))

def dyn(C):
    N = len(C)
    F = [[0,0] for _ in range(N+1)]
    for i in range(1,N+1):
        F[i][0] = max(F[i-1][0],F[i-1][1])
        F[i][1] = F[i-1][0] + C[i-1]
    return max(F[N][0],F[N][1])



print(C)
#print(max(f(N-1,True),f(N-1,False)))
print(dyn(C))