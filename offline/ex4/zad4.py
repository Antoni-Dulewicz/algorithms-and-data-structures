#ANTONI DULEWICZ
"""
Program najpierw znajduje najkrotsza sciezke w grafie pomiedzy s i t za pomoca algorytmu BFS.
Nastepnie z tej sciezki usuwa kolejne krawedzie i dla kazdej usunietej krawedzi znowu liczy 
najkrotsza sciezke miedzy s i t. Jesli dlugosc nowo policzonej sciezki jest inna niz dlugosc sciezki
z poczatku to program sie konczy zwracajac wierzcholki usunietej krawedzi. Jesli dlugosci sa takie
same to program wstawia spowrotem krawedz, usuwa nastepna w sciezce i powtarza proces.  
"""
"""
Zlozonosc obliczeniowa: O(k*(V+E))
V - wierzcholki grafu
E - krawedzie
k - dlugosc n
ajkrotszej sciezki
"""
from zad4testy import runtests
"""from math import inf
from collections import deque
def shortest(G,s,t):
    n = len(G)
    visited = [0 for _ in range(n)]
    prev = [-1 for _ in range(n)]
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while len(queue):
        curr = queue.popleft()
        curr_len = len(G[curr])
        for i in range(curr_len):
            idx = G[curr][i]
            if idx != -1:
                if not visited[idx]:
                    prev[idx] = curr
                    visited[idx] = 1
                    queue.append(idx)
    
    if visited[t] == 0:
        return None,inf
    
    if prev[t] == s:
        return [s,t],1
    
    path = [t]
    first_len = 0
    ind = t
    while ind != s:
        first_len += 1
        path += [prev[ind]]
        ind = prev[ind]
    return path,first_len

def delete(G,p,q):

    for i in range(len(G[p])):
        if G[p][i] == q:
            curr_P_idx = i
            curr_P = G[p][i] 
            G[p][i] = -1
    
    for i in range(len(G[q])):
        if G[q][i] == p:
            curr_Q_idx = i
            curr_Q = i
            G[q][i] = -1
    return curr_P,curr_P_idx,curr_Q,curr_Q_idx
    

def check_if(G,p,q,s,t):
    curr_P,curr_P_idx,curr_Q,curr_Q_idx = delete(G,p,q)
    curr_path,curr_short = shortest(G,s,t)
    return curr_P,curr_P_idx,curr_Q,curr_Q_idx,curr_short


def longer(G,s,t):
    path,short = shortest(G,s,t)
    for i in range(len(path)-1):
        p = path[i]
        q = path[i+1]
        curr_P,curr_P_idx,curr_Q,curr_Q_idx,curr_short = check_if(G,p,q,s,t)
        if curr_short != short:
            return p,q
        G[p][curr_P_idx] = curr_P
        G[q][curr_Q_idx] = curr_Q
    return None    
"""
"""from collections import deque
def delete_edge(G,u,v):
    for i in range(len(G[u])):
        if G[u][i] == v:
            G[u][i] = -1
            
    for i in range(len(G[v])):
        if G[v][i] == u:
            G[v][i] = -1
    
def add_edge(G,u,v):    
    for i in range(len(G[u])):
        if G[u][i] == -1:
            G[u][i] = v

    for i in range(len(G[v])):
        if G[v][i] == -1:
            G[v][i] = u


def shortest(G,s,t):
    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]

    q = deque()
    q.append(s)
    visited[s] = 1

    while len(q):
        u = q.popleft()

        for v in G[u]:
            idx = v

            if idx != -1:

                if not visited[idx]:
                    parent[idx] = u
                    visited[idx] = 1
                    q.append(idx)

    if visited[t] == 0:
        return None,float('inf')                

    if parent[t] == s:
        return [s,t],1

    path = []
    idx = t

    while idx != s:
        path.append(idx)
        idx = parent[idx]

    path.append(s)

    return path,len(path)-1



def longer(G,s,t):
    path,short = shortest(G,s,t)
    for i in range(len(path)-1):
        curr_u = path[i]
        curr_v = path[i+1]

        delete_edge(G,curr_u,curr_v)

        tmp_path,tmp_path_len = shortest(G,s,t)

        if tmp_path_len != short:
            return curr_u,curr_v
        
        add_edge(G,curr_u,curr_v)

    return None
"""

from collections import deque

def shortest(G,s,t):
    n = len(G)
    visited = [False for _ in range(n)]
    prev = [-1 for _ in range(n)]
    q = deque()
    q.append(s)
    visited[s] = True
    while len(q):
        u = q.popleft()
        for v in G[u]:
            if v != -1:    
                if not visited[v]:
                    prev[v] = u
                    visited[v] = True
                    q.append(v)

    if visited[t] == 0:
        return None,float('inf')

    if prev[t] == s:
        return [s,t],1

    path = []
    idx = t
    while idx != s:
        path.append(idx)
        idx = prev[idx]
    path.append(s)
    return path,len(path)

def remove_edge(G,u,v):
    for i in range(len(G[u])):
        if G[u][i] == v:
            G[u][i] = -1
            

    for i in range(len(G[v])):
        if G[v][i] == u:
            G[v][i] = -1
            

def add_edge(G,u,v):
    for i in range(len(G[u])):
        if G[u][i] == -1:
            G[u][i] = v

    for i in range(len(G[v])):
        if G[v][i] == -1:
            G[v][i] = u


def longer(G,s,t):

    shortest_path,shortest_len = shortest(G,s,t)
    for i in range(1,shortest_len):
        u = shortest_path[i-1]
        v = shortest_path[i]
        remove_edge(G,u,v)
        curr_path,curr_len = shortest(G,s,t)
        if curr_len > shortest_len:
            return u,v
        add_edge(G,u,v)

    return  None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )