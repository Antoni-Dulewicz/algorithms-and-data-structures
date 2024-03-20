from math import inf
def floyd(G):
    n = len(G)

    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                G[i][j] = float('inf')
            
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j],G[i][k] + G[k][j])
    
    for i in range(n):
        G[i][i] = inf
    return G

"""G = [[0,3,0,5],
     [2,0,0,4],
     [0,1,0,0],
     [0,0,2,0]]"""

G = [[0,2,0,0,0],
     [0,0,3,4,4],
     [4,0,0,-4,0],
     [0,0,0,0,0],
     [0,0,0,1,0]]
res = floyd(G)
for w in res:
    print(w)