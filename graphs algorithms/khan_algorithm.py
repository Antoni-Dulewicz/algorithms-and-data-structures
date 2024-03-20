# To find topological ordering (top. sort)
from collections import deque

def khan(G):
    n = len(G)
    ins = [0 for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            ins[G[i][j]] += 1
    
    q = deque()

    for i in range(n):
        if ins[i] == 0:
            ins[i] = -1
            q.append(i)
    
    path = []

    while len(q):
        u = q.popleft()
        path.append(u)

        for v in G[u]:
            ins[v] -= 1
        G[u] = []

        for i in range(n):
            if ins[i] == 0:
                ins[i] = -1
                q.append(i)    

    return path

G = [[2,3,6],
     [4],
     [6],
     [1,4],
     [5,8],
     [],
     [7,11],
     [4,12],
     [],
     [2,10],
     [6],
     [12],
     [8],
     []]

print(khan(G))