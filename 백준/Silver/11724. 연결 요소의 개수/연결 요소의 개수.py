
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
