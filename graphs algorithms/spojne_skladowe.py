def reverse_edges(G):
    res = []
    for i in range(len(G)):
        res.append([])
    for i in range(len(G)):
        for x in G[i]:
            res[x].append(i)
    return res

def find_max(T):
    res = 0
    for i in range(len(T)):
        if T[res] < T[i]:
            res = i
    T[res] = -1
    return res
        

def spojne(G):
    n = len(G)
    visited = [0 for _ in range(n)]
    time = 0
    parent = [-1 for _ in range(n)]
    times = [0 for _ in range(n)]
    def DFSVisit(G,u):
        nonlocal time
        visited[u] = 1
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G,v)
        time += 1
        times[u] = time

    for u in range(n):
        if not visited[u]:
            DFSVisit(G,u)
    
    G = reverse_edges(G)
    def Visit(G,u):
        visited[u] = 1
        nonlocal tmp
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                tmp += [v]
                Visit(G,v)
        
        times[u] = -1

    visited = [0 for _ in range(n)]

    while min(visited) == 0:
        tmp = []
        u = find_max(times)
        tmp += [u]
        if not visited[u]:
            Visit(G,u)
        print(tmp)
    
    return time

G = [[1],
     [2],
     [0,3,8],
     [4,6],
     [5],
     [3],
     [5],
     [8],
     [9],
     [5,10],
     [3,7]]
print(spojne(G))