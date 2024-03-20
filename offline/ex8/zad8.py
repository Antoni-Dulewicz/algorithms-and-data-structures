#ANTONI DULEWICZ
from zad8testy import runtests
from queue import PriorityQueue


"""Prpgram przygotowuje dane w ten sposob aby ilosc litrow w z jednej plamy byla zapisana w jednej komorce tablicy. Nastepnie przechodzi po tablicy
zapisujac kolejne wartosci plam w kolejce priorytetowej jednoczesnie zmiejszajac ilosc paliwa ktore mamy w aucie. Jesli paliwo sie skonczy to bierzemy
najwieksza wartosc wczesniej zapisana w kolejce jednoczesnie zwiekszajac ilosc tankowan (postojow). 
"""
#Zlozonosc: O(nm + nlogn), gdzie n to dlugosc trasy a m to szerokosc na ktorej sa plamy 


"""def contains(T,w,k):
    n = len(T)
    m = len(T[0])
    return w >= 0 and w < n and k >= 0 and k < m


def prepare_data(T):
    n = len(T[0])
    dp = [0 for _ in range(n)]
    

    def collect_gas(T,w,k):
        nonlocal gas
        gas += T[w][k]
        T[w][k] = 0
        moves = [(1,0),(0,1),(0,-1),(-1,0)]
        for x in moves:
            new_w = w + x[0]
            new_k = k + x[1]
            if contains(T,new_w,new_k):
                if T[new_w][new_k] != 0:
                    collect_gas(T,new_w,new_k)
        return gas

    
    for i in range(n):
        if T[0][i] != 0:
            gas = 0
            collect_gas(T,0,i)
            dp[i] = gas
    return dp

def plan(T):
    dp = prepare_data(T)
    n = len(dp)
    how_many_pumps = 1
    spils = PriorityQueue()
    gas = dp[0]
    for i in range(1,n):
        if gas == 0:
            gas = (-1)*spils.get()
            how_many_pumps += 1
        if dp[i] != 0:
            spils.put(-dp[i])
        gas -= 1

    return how_many_pumps
"""

from math import inf
def contains(T,w,k):
    n = len(T)
    m = len(T[0])
    return w >= 0 and w < n and k >= 0 and k < m


def prepare_data(T):
    n = len(T[0])
    new_tab = [0 for _ in range(n)]
    

    def pump_gas(T,w,k):
        nonlocal gas
        gas += T[w][k]
        T[w][k] = 0
        moves = [(1,0),(0,1),(0,-1),(-1,0)]
        for x in moves:
            new_w = w + x[0]
            new_k = k + x[1]
            if contains(T,new_w,new_k):
                if T[new_w][new_k] != 0:
                    pump_gas(T,new_w,new_k)
        return gas

    
    for i in range(n):
        if T[0][i] != 0:
            gas = 0
            pump_gas(T,0,i)
            new_tab[i] = gas

    res = []
    for i in range(n):
        if new_tab[i] != 0:
            res += [(i,new_tab[i])]
    return res

def plan(T):
    print(*T,sep='\n')
    target = len(T[0])-1
    spils = prepare_data(T)
    n = len(spils)
    dp = [0 for _ in range(n)]
    start = spils[0][1]
    spils.pop(0)
    n = len(spils)
    dp[0] = start
    
    for i in range(n):
        location = spils[i][0]
        capacity = spils[i][1]
        for t in range(i,-1,-1):
            if dp[t] >= location:
                dp[t+1] = max(dp[t+1],dp[t] + capacity)
            
    for i in range(len(dp)):
        if dp[i] >= target: return i + 1
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = False )

