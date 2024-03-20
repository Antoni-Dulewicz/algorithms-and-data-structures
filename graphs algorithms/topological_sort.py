def topologic(G):
    n = len(G)
    sorted = []
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    def DFSVisit(G,v):
        nonlocal sorted
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                DFSVisit(G,u)
        sorted.append(v)
    for u in range(n):
        if not visited[u]:
            DFSVisit(G,u)
    return sorted[::-1]
    
G = [[1],
     [2],
     [],
     [2],
     [1,2,3],
     [1,4]]
    
print(topologic(G))