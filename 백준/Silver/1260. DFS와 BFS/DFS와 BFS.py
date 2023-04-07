from collections import deque

n, m, v = map(int, input().split())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    graph[v].sort()
    visited[v] = 1
    print(v, end=" ")

    for node in graph[v]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0

    while q:
        x = q.popleft()
        print(x, end=" ")

        for node in graph[x]:
            if visited[node] == 1:
                visited[node] = 0
                q.append(node)

dfs(v)
print()
bfs(v)