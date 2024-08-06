from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = False
    
    while q:
        x = q.popleft()
        print(x, end = " ")
        
        for next_node in matrix[x]:
            if visited[next_node]:
                visited[next_node] = False
                q.append(next_node)

def dfs(v):
    visited[v] = True
    print(v, end = " ")
    
    for next_node in matrix[v]:
        if not visited[next_node]:
            dfs(next_node)

    
n, m, v = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for m in matrix:
    m.sort()
    
dfs(v)
print()
bfs(v)