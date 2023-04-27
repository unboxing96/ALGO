from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [-1] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if parent[i] == -1:
                parent[i] = now
                q.append(i)

bfs(1)

for i in range(2, n + 1):
    print(parent[i])