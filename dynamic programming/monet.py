from random import randint
#wydawanie monet, w dowolnej liczbie (moga sie powtarzac)
#mamy monety i dana kwota
#np 1,5,8 i kwota: 15
#DYNAMIK
def coins_rek(T,val):
    F = [None for _ in range(val+1)]
    F[0] = 0
    if val < 0:
        return float('inf')
    if F[val] is None:
        F[val] = min(coins_rek(T,val-x) for x in T) + 1

def coins(T,val):
    F = [float('inf') for _ in range(val+1)]
    F[0] = 0
    for i in range(val+1):
        for coin in T:
            if i + coin <= val:
                F[i+coin] = min(F[i+coin],F[i]) + 1
                
    return F[val]

n = 10
T = [randint(1,9)for _ in range(n)]
print(*T,sep = ' ')
print(coins(T,10))

