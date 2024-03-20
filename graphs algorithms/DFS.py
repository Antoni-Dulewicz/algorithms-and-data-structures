def DFS(T):
    n = len(T[0])
    time = 0
    def DFSvisit(T,u):
        n = len(T)
        nonlocal time
        time += 1
        visited[u] = 1
        for i in range(n):
            if T[u][i] and not visited[i]:
                parent[i] = u
                DFSvisit(T,i)
        time += 1

    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    
    for u in range(n):
        if not visited[u]:
            DFSvisit(T,u)
    return parent


T = [[0,1,0,1,0,0,1],
     [1,0,0,1,0,0,0],
     [0,0,0,0,1,0,0],
     [1,1,0,0,0,0,0],
     [0,0,1,0,0,1,1],
     [0,0,0,0,1,0,0],
     [1,0,0,0,1,0,0]]

print(DFS(T))