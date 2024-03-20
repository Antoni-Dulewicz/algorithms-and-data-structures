    #KRUSKAL ALGORITHM
"""
finding MST (minimal spanning tree in graph) using union-find date structure
"""
def find(x,parent):
    if parent[x] != x:
        parent[x] = find(parent[x],parent)
    return parent[x]
def union(x,y,parent,rank):
    x = find(x,parent)
    y = find(y,parent)
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def kruskal(G,n):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    result = []
    
    cnt = 0
    i = 0

    G.sort(key=lambda item: item[2])

    while cnt < n-1:
        u,v,weight = G[i]
        x = find(u,parent)
        y = find(v,parent)

        if x != y:
            result.append((u,v,weight))
            union(u,v,parent,rank)
            cnt += 1
        
        i += 1
    
    cost = 0
    for u,v,weight in result:
        print("%d -- %d = %d" % (u,v,weight))
        cost += weight
    return cost,result


G = [[0,1,2],
     [1,2,3],
     [1,4,4],
     [2,0,7],
     [2,3,6],
     [3,1,4],
     [4,3,1]]

print(kruskal(G,5))