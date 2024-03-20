# dopoki istnieje sciezka:
# 1. znajdz gardlo sciezki 
# 2. zwieksza maksymalny przeplyw o flow
# 3. zmodyfikuj znaleziona sciezke 
# 4. sprawdz nastepna sciezke 

def BFS(G,s,t,parent):
    n = len(G)
    visited = [False for _ in range(n)]
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop()

        for v in range(n):
            if G[u][v] > 0:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    parent[v] = u
                    if v == t:
                        return True
    return False

def ford_fulkerson(G,source,sink):
    n = len(G)
    parent = [-1 for _ in range(n)]

    max_flow = 0

    while BFS(G,source,sink,parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow,G[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]
    
    return max_flow


graph1 = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

graph2 = [[0,10,0,10,0,0],
         [0,0,4,2,8,0],
         [0,0,0,0,0,10],
         [0,0,0,0,9,0],
         [0,0,6,0,0,10],
         [0,0,0,0,0,0]]

graph = [[0,0,1,1,0],
         [1,1,0,1,0],
         [1,0,1,0,0],
         [0,1,0,1,1],
         [0,0,1,1,0]]

print(ford_fulkerson(graph,0,4))