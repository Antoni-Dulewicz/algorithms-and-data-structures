#ANTONI DULEWICZ
from zad5testy import runtests
import heapq
"""Program "laczy" w jeden wierzcholek (n) punkty zakrzywienia czasoprzestrzeni a nastepnie odpala
algorytm Dijkstry znajdujac najkrotsza sciezke miedzy a i b. Jeśli punkt a lub b dla którego ma
znalezc odleglosc jest jednym z punktow zakrzywienia to program znajduje drogę od n (wierzcholka
stworzonego z punktow zakrzywienia) do odpowiednio a lub b. Jesli a i b to ten sam wierzcholek 
(lub oba sa punktami zakrzywienia) to program zwraca wartosc zero."""
#Zlozonosc: O(E*logV) (funckcja prepare: E+S, dijkstra: E*logV)

def contains(num,S):
    for x in S:
        if num == x:
            return True
    return False

def prepare(n,E,S):
    s = len(S)
    e = len(E)
    tmp = [0 for _ in range(n)]

    for i in range(s):
        tmp[S[i]] = 1

    for i in range(e):
        if tmp[E[i][0]]:
            E[i] = (n,E[i][1],E[i][2])
        if tmp[E[i][1]]:
            E[i] = (E[i][0],n,E[i][2])
    
    G = [[] for _ in range(n+1)]
    for first,second,weight in E:
        G[first].append((second,weight))
        G[second].append((first,weight))
    return G


def spacetravel( n, E, S, a, b ):
    if contains(a,S):
        a = n
    if contains(b,S):
        b = n
    if a == b:
        return 0 
    
    G = prepare(n,E,S)

    cost = [float('inf') for _ in range(n+1)]
    q = []
    cost[a] = 0
    heapq.heappush(q,(0,a))
    while len(q):
        d,v = heapq.heappop(q)
        for u,weight in G[v]:
            if cost[u] > cost[v] + weight:
                cost[u] = cost[v] + weight
                heapq.heappush(q,(cost[u],u))

    if cost[b] == float('inf'):
        return None
    
    return cost[b]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )