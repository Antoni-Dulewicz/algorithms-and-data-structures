def bellman_ford(G,s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    distance[s] = 0
    for v in range(n):

        for u,weight in G[v]:
            if distance[u] > distance[v] + weight:
                distance[u] = distance[v] + weight
                parent[u] = v
                
    for v in range(n):
        for u,weight in G[v]:
            if distance[u] > distance[v] + weight:
                print("Graph contains negative circles")
                return 
            
    return distance,parent

G = [
    [(1, 2)],
    [(2, 3), (4, 4)],
    [(0, 4), (3, -4)],
    [(1, 4)],
    [(3, 1)]
]
"""
G = [[0,1,2],
     [1,2,3],
     [1,4,4],
     [2,0,7],
     [2,3,6],
     [3,1,4],
     [4,3,1]]
"""
print(bellman_ford(G,0))