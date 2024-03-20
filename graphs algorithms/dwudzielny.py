from collections import deque
def czy_dwudzielny(T,s):
    n = len(T[0])
    visited = [0 for _ in range(n)]
    odd = [-1 for _ in range(n)]
    visited[s] = 1
    odd[s] = 0
    queue = deque()
    queue.append(s)
    while len(queue):
        curr = queue.pop()
        for i in range(n):
            if T[curr][i]:
                if not visited[i]:
                    visited[i] = 1
                    odd[i] = 1 - odd[curr]
                    queue.append(i)
                elif odd[i] == odd[curr]:
                    return False
    return True

# czy graf dwudzielny?
T = [[0,1,0,0,0], # 0
     [0,0,1,0,1], # 1
     [0,1,0,1,0], # 2
     [0,0,1,0,0], # 3
     [0,1,0,1,0]] # 4

print(czy_dwudzielny(T,0))