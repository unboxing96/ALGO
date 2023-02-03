from collections import deque


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    q.append(v)
    visited[v] = False

    while q:
        x = q.popleft()
        print(x, end=" ")

        for i in graph[x]:
            if visited[i]:
                q.append(i)
                visited[i] = False


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(v)
print("")
bfs(v)
