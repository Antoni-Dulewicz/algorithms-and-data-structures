#ANTONI DULEWICZ
from zad6testy import runtests
"""
Program dodaje wierzcholek s oraz t do danego grafu dwudzielnego (skierowanego) a następnie
wyznacza najwieksze skojarzenie w grafie uzywajac algorytmu Forda-Fulkersona (do znajdowania maks
przeplywu w grafie). W rep listowej nie musimy nadawac wag bo dal kazdej krawedzi beda o wartosci 1. 
"""
# Zlozonosc O(V^3)

def prepare_list(M): #przygotowanie danych (dodanie s i t i zapisanie grafu w postaci listowej)
    n = len(M)
    s = [0 for _ in range(n)]
    
    for i in range(n):
        s[i] = i+1
        
    res = []
    res.append(s)

    for x in range(n):
        for y in range(len(M[x])):
            tmp = M[x][y] + n+1
            M[x][y] = tmp

    for i in range(n):
        res.append(M[i])

    for i in range(n):
        res.append([2*n+1])
    
    res.append([])
                       

    return res,0,2*n+1,2*n+2

def check_path(G,s,t,parent): #znalezienie sciezki miedzy s i t za pomoca algorytmu DFS
    n = len(G)
    visited = [0 for _ in range(n)]
    stack = []
    stack.append(s)

    while len(stack):
        u = stack.pop()

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                if v == t:
                    return True
                visited[u] = 1
                stack.append(v)
                
    return False

def binworker(M): # FORD-FULKERSON
    M,s,t,n = prepare_list(M)

    parent = [-1 for _ in range(n)]
    workers = 0


    while check_path(M,s,t,parent):

        workers += 1
        
        v = t
        while(v != s):
            u = parent[v]
            M[v] += [u]
            M[u].remove(v)
            v = parent[v]

    return workers


"""from collections import deque
def prepare_data(M):
    n = len(M)
    G = [[] for _ in range(2*n + 2)]

    for i in range(n):
        G[0].append(i+1)

    for i in range(n):
        for j in range(len(M[i])):

            G[i + 1].append(M[i][j] + n + 1)

    for i in range(n+1,2*n+1):
        G[i].append(2*n+1)

    return G

def BFS(G,s,t,parent):
    n = len(G)
    visited = [False for _ in range(n)]

    q = deque()
    q.append(s)
    visited[s] = True
    while len(q):
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                if v == t:
                    return True
                q.append(v)

    return False


def ford_fulkerson(G,source,sink):
    n = len(G)
    parent = [-1 for _ in range(n)]

    max_flow = 0

    while BFS(G,source,sink,parent):
        
        max_flow += 1

        v = sink
        while v != source:
            u = parent[v]
            G[v].append(u)
            G[u].remove(v)
            v = parent[v]      

    return max_flow



def binworker(M):
    G = prepare_data(M)
    return ford_fulkerson(G,0,len(G)-1)
"""

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
