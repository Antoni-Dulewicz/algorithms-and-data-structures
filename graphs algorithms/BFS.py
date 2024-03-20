from collections import deque
def BFS(T,s):
    n = len(T[0])
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    d = [0 for _ in range(n)]
    d[s] = 0
    visited[s] = 1
    queue = deque()
    queue.append(s)
    while len(queue):
        curr = queue.popleft()
        for i in range(n):
            if T[curr][i] and not visited[i]:
                parent[i] = curr
                visited[i] = 1
                d[i] = d[curr] + 1
                queue.append(i)
    return d,parent,visited

T = [[0,1,1,0,0,0,0,0],
     [1,0,0,0,1,0,0,0],
     [1,0,0,1,0,1,0,0],
     [0,0,1,0,1,0,0,0],
     [0,1,0,1,0,1,0,0],
     [0,0,1,0,1,0,1,0],
     [0,0,0,0,0,1,0,1],
     [0,0,0,0,0,0,1,0]]
print(BFS(T,0))