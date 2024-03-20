from queue import PriorityQueue

"""def prime_for_matrix(G):
    n = len(G)
    visited = [0 for _ in range(n)]
    mst_array = []
    q = PriorityQueue()
    q.put((0,0,0))
    u = 0
    visited[u] = 1
    for _ in range(n-1):
        for v in range(n):
            if G[u][v] and not visited[v]:
                weight = G[u][v]
                q.put((weight,u,v))
        
        w,u,v = q.get()
        while visited[v]:
            w,u,v = q.get()
        
        visited[v] = 1
        mst_array += [(u,v,w)]
        u = v
    return mst_array
"""       
"""def prime_for_list(G):
    n = len(G)
    mst_array = []
    visited = [0 for _ in range(n)]
    q = PriorityQueue()
    q.put((0,0,0))
    u = 0
    visited[u] = 1
    for _ in range(n-1):
        for v,weight in G[u]:
            if not visited[v]:
                q.put((weight,u,v))
        
        weight,u,v = q.get()
        while visited[v]:
            weight,u,v = q.get()
        
        visited[v] = 1
        mst_array += [(u,v,weight)]
        u = v
    return mst_array
"""

def minKey(G,key,mstSet):
    n = len(G)
    mini = float('inf')
    for v in range(n):
        if key[v] < mini and not mstSet[v]:
            mini = key[v]
            min_index = v

    return min_index

def prim(G):
    n = len(G)
    key = [float('inf') for _ in range(n)] #tablica wierzcholkow 
    parent = [-1 for _ in range(n)]

    key[0] = 0
    mstSet = [False for _ in range(n)] #tablica wzietych wierzcholkow do mst

    
    mst_cost = 0
    
    # przechodzimy po wszystkich wierzcholkach 

    for _ in range(n):
        #znajdujemy najemniejszy wierzcholek sasiadujacy z mst
        u = minKey(G,key,mstSet)

        #dodajemy najmniejszy wierzcholek do mst
        mstSet[u] = True

        # przegladamy wierzcholki sasaidujace z najmniejszym 
        # i dodajemy je do tablicy wierzcholkow
        for v,weight in G[u]:
            if  not mstSet[v] and key[v] > weight:
                key[v] = weight
                parent[v] = u


    for i in range(n):
        mst_cost += key[i]
    

    return parent,mst_cost


"""
G_l = [[(1,2),(2,7)],
     [(0,2),(2,3),(3,4),(4,4)],
     [(0,7),(1,3),(3,6)],
     [(2,6),(1,4),(4,1)],
     [(3,1)]]


G_m = [[0,2,0,0,0],
     [2,0,3,4,5],
     [7,3,0,6,0],
     [0,4,6,0,1],
     [0,5,0,1,0]] """
G = [[(1,4),(2,6)],
     [(0,4),(2,6),(3,3),(4,4)],
     [(0,6),(1,6),(3,1)],
     [(1,3),(2,1),(4,2),(5,3)],
     [(1,4),(3,2),(5,7)],
     [(3,3),(4,7)]]

"""G = [[0,4,6,0,0,0],
     [4,0,6,3,4,0],
     [6,6,0,1,0,0],
     [0,3,1,0,4,3],
     [0,4,0,2,0,7],
     [0,0,0,3,7,0]]"""
print(prim(G))