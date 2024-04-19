def dfs(now):
    visited[now] = True
    print(now, end = " ")

    for next in matrix[now]:
        if not visited[next]:
            dfs(next)

def bfs(now):
    q = deque([now])
    visited[now] = True

    while q:
        x = q.popleft()
        print(x, end = " ")

        for next in matrix[x]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


from collections import deque

n, m, v = map(int, input().split())
matrix = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for row in matrix:
    row.sort()

visited = [False] * (n + 1)
dfs(v)

print()

visited = [False] * (n + 1)
bfs(v)