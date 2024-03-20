#DIJSKTRA FOR LIST
from queue import PriorityQueue

def dijkstra(G, s):
    distance = [float("inf") for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    q = PriorityQueue()
    distance[s] = 0
    q.put((0, s))
    while not q.empty():
        d, v = q.get()

        for u, waga in G[v]:
            if distance[u] > distance[v] + waga:
                parent[u] = v
                distance[u] = distance[v] + waga
                q.put((distance[u], u))


    return parent,distance


G = [
    [(1, 2), (2, 7)],
    [(0, 2), (2, 3), (4, 4)],
    [(0, 7), (3, 6)],
    [(2, 6), (1, 4)],
    [(1, 4), (3, 1)]
]

print(dijkstra(G, 0))


#DIJKSTRA FOR MATRIX
def dijkstra(G,s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    q = PriorityQueue()
    distance[s] = 0
    q.put((0,s))
    while not q.empty():
        d,v = q.get()

        for u in range(n):
            if G[v][u]:
                if distance[u] > distance[v] + G[v][u]:
                    parent[u] = v
                    distance[u] = distance[v] + G[v][u]
                    q.put((distance[u],u))

    return parent,distance
    
"""G = [[0,2,7,0,0],
     [2,0,3,0,4],
     [7,0,0,6,0],
     [0,4,6,0,0],
     [0,4,0,1,0]]

print(dijkstra(G, 0))"""

# DIJKSTRA ON LIST USING BINARY HEAP
"""import heapq
def dijkstra(G,s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    q = []
    distance[s] = 0
    heapq.heappush(q,(0,s))
    while len(q):
        d,curr = heapq.heappop(q)

        for neighbor,weight in G[curr]:
            if distance[neighbor] > distance[curr] + weight:
                distance[neighbor] = distance[curr] + weight
                parent[neighbor] = curr
                heapq.heappush(q,(distance[neighbor],neighbor))
    return parent,distance
"""